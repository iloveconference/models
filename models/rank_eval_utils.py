"""Utility functions for analyzing logs."""

import gzip
import json
import zlib
from typing import Any

import boto3  # type: ignore
from tqdm import tqdm


_GZIP_MAGIC = b"\x1f\x8b"
_JSON_WHITESPACE = " \t\n\r"


def load_logs(bucket_name: str, prefix: str = "") -> list[dict[str, Any]]:
    """Load CloudWatch Logs subscription envelopes from an S3 bucket.

    Firehose writes each envelope it receives from CloudWatch Logs as-is, so an object holds
    several envelopes back to back, either as concatenated gzip members or as plain JSON
    (possibly separated by whitespace).

    Args:
        bucket_name: The bucket the Firehose delivery stream writes to.
        prefix: Only read objects whose keys start with this prefix.

    Returns:
        The envelopes from every object, in key order.

    Raises:
        ValueError: If an object is corrupt gzip, isn't UTF-8, or isn't a sequence of JSON objects.
    """
    s3 = boto3.client("s3")

    keys: list[str] = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket_name, Prefix=prefix):
        keys.extend(obj["Key"] for obj in page.get("Contents", []))

    envelopes = []
    for key in tqdm(keys):
        body = s3.get_object(Bucket=bucket_name, Key=key)["Body"].read()
        try:
            envelopes.extend(_parse_json_objects(_decode_body(body)))
        except (EOFError, gzip.BadGzipFile, zlib.error, ValueError) as err:
            raise ValueError(f"Could not read s3://{bucket_name}/{key}: {err}") from err
    return envelopes


def _decode_body(body: bytes) -> str:
    """Return an S3 object's text, gunzipping it first if it starts with the gzip magic bytes."""
    if body[:2] == _GZIP_MAGIC:
        body = gzip.decompress(body)
    return body.decode("utf-8")


def _parse_json_objects(text: str) -> list[dict[str, Any]]:
    """Parse JSON objects written back to back, optionally separated by whitespace."""
    decoder = json.JSONDecoder()
    objects = []
    pos = _skip_whitespace(text, 0)
    while pos < len(text):
        start = pos
        obj, pos = decoder.raw_decode(text, pos)
        if not isinstance(obj, dict):
            raise ValueError(f"expected a JSON object at char {start}, found {type(obj).__name__}")
        objects.append(obj)
        pos = _skip_whitespace(text, pos)
    return objects


def _skip_whitespace(text: str, pos: int) -> int:
    """Return the index of the first non-whitespace character in text at or after pos."""
    while pos < len(text) and text[pos] in _JSON_WHITESPACE:
        pos += 1
    return pos


def get_log_messages(logs: list[dict[str, Any]], message_type: str) -> list[dict[str, Any]]:
    """Get log messages of a specific type.

    Envelopes other than DATA_MESSAGEs are skipped (CloudWatch Logs sends a CONTROL_MESSAGE
    when a subscription filter is created), as are log events whose message isn't a JSON object.

    Args:
        logs: CloudWatch Logs subscription envelopes, as returned by load_logs.
        message_type: The value of the "message" field of the log records to return, e.g. "search".

    Returns:
        The parsed log records whose "message" field equals message_type.
    """
    messages = []
    for log in logs:
        if log.get("messageType") != "DATA_MESSAGE":
            continue
        for log_event in log.get("logEvents", []):
            if "message" not in log_event:
                continue
            try:
                message = json.loads(log_event["message"])
            except json.JSONDecodeError:
                continue
            if not isinstance(message, dict) or message.get("message") != message_type:
                continue
            messages.append(message)
    return messages
