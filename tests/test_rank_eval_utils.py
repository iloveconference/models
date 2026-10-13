"""Test cases for the rank_eval_utils module."""

import gzip
import io
import json
import re
from pathlib import Path
from typing import Any
from typing import Iterator

import boto3  # type: ignore
import pytest
from botocore import UNSIGNED  # type: ignore
from botocore.config import Config  # type: ignore
from botocore.response import StreamingBody  # type: ignore
from botocore.stub import Stubber  # type: ignore

from models import rank_eval_utils


BUCKET = "iloveconference.logs"

# What CloudWatch Logs sends through a subscription when the filter is created.
CONTROL_MESSAGE: dict[str, Any] = {
    "messageType": "CONTROL_MESSAGE",
    "owner": "CloudwatchLogs",
    "logGroup": "",
    "logStream": "",
    "subscriptionFilters": [],
    "logEvents": [
        {
            "id": "",
            "timestamp": 1760378400000,
            "message": "CWL CONTROL MESSAGE: Checking health of destination Firehose.",
        }
    ],
}


def _search_record(q: str) -> str:
    """Return a "search" log line like the ones the server writes."""
    return json.dumps(
        {
            "asctime": "2026-10-13 18:00:00,000",
            "name": "server.main",
            "levelname": "INFO",
            "message": "search",
            "role": "role",
            "prefix": "prefix",
            "response": {"q": q, "session": 1, "answer": "answer", "results": []},
        }
    )


def _data_message(*messages: str) -> dict[str, Any]:
    """Return a DATA_MESSAGE envelope holding one log event per message."""
    return {
        "messageType": "DATA_MESSAGE",
        "owner": "123456789012",
        "logGroup": "/aws/lambda/ilc-search",
        "logStream": "2026/10/13/[$LATEST]0123456789abcdef0123456789abcdef",
        "subscriptionFilters": ["server"],
        "logEvents": [
            {"id": str(i), "timestamp": 1760378400000 + i, "message": message} for i, message in enumerate(messages)
        ],
    }


def _firehose_gzip(*envelopes: dict[str, Any]) -> bytes:
    """Return an object body as Firehose writes CloudWatch Logs records: one gzip member per envelope."""
    return b"".join(gzip.compress(json.dumps(envelope).encode()) for envelope in envelopes)


def _queries(log_messages: list[dict[str, Any]]) -> list[str]:
    """Return the query of each "search" log record."""
    return [log_message["response"]["q"] for log_message in log_messages]


@pytest.fixture
def s3(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Iterator[Stubber]:
    """Make boto3.client return an S3 client whose responses are stubbed, so nothing reaches AWS."""
    # Ignore the developer's AWS profile and config: an AWS_PROFILE missing from them fails client creation.
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.delenv("AWS_DEFAULT_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", str(tmp_path / "config"))
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", str(tmp_path / "credentials"))
    # Unsigned, so botocore never looks for credentials: the stubber answers every call.
    client = boto3.Session(region_name="us-west-2").client("s3", config=Config(signature_version=UNSIGNED))
    monkeypatch.setattr(boto3, "client", lambda service_name, **kwargs: client)
    with Stubber(client) as stubber:
        yield stubber
        stubber.assert_no_pending_responses()


def _stub_list_page(
    s3: Stubber, keys: list[str], prefix: str = "", page: str | None = None, next_page: str | None = None
) -> None:
    """Queue a list_objects_v2 page, requested with continuation token page; next_page marks it truncated."""
    expected_params: dict[str, Any] = {"Bucket": BUCKET, "Prefix": prefix}
    if page is not None:
        expected_params["ContinuationToken"] = page
    response: dict[str, Any] = {"IsTruncated": next_page is not None, "KeyCount": len(keys), "Prefix": prefix}
    if keys:
        response["Contents"] = [{"Key": key, "Size": 1024} for key in keys]
    if next_page is not None:
        response["NextContinuationToken"] = next_page
    s3.add_response("list_objects_v2", response, expected_params)


def _stub_get_object(s3: Stubber, key: str, body: bytes, content_type: str = "application/octet-stream") -> None:
    """Queue a get_object response."""
    response = {
        "Body": StreamingBody(io.BytesIO(body), len(body)),
        "ContentLength": len(body),
        "ContentType": content_type,
    }
    s3.add_response("get_object", response, {"Bucket": BUCKET, "Key": key})


def test_get_log_messages() -> None:
    """It returns log messages."""
    log = {
        "messageType": "DATA_MESSAGE",
        "subscriptionFilters": ["server"],
        "logEvents": [
            {
                "message": """{
                "asctime": "2023-03-01 01:11:19,394",
                "name": "server.main",
                "levelname": "INFO",
                "message": "search",
                "prompt": "prompt",
                "response": {
                    "q": "question",
                    "session": 3287431778,
                    "answer": "answer.",
                    "results": [{
                        "id": 20635,
                        "title": "title",
                        "author": "author",
                        "year": "2016",
                        "month": "04",
                        "url": "url",
                        "text": "text."
                    }, {
                        "id": 88026,
                        "title": "title2",
                        "author": "author2",
                        "year": "2014",
                        "month": "10",
                        "url": "url2",
                        "text": "text2"
                    }]
                }
            }""",
            },
            {
                "message": """{
                "asctime": "2023-03-01 01:11:19,394",
                "name": "server.main",
                "levelname": "INFO",
                "message": "search",
                "prompt": "prompt2",
                "response": {
                    "q": "question2",
                    "session": 3287431778,
                    "answer": "answer2.",
                    "results": [{
                        "id": 20635,
                        "title": "title3",
                        "author": "author3",
                        "year": "2016",
                        "month": "04",
                        "url": "url3",
                        "text": "text3."
                    }, {
                        "id": 88026,
                        "title": "title4",
                        "author": "author4",
                        "year": "2014",
                        "month": "10",
                        "url": "url4",
                        "text": "text4"
                    }]
                }
            }""",
            },
        ],
    }

    log_messages = rank_eval_utils.get_log_messages([log], "search")
    assert len(log_messages) == 2
    assert log_messages[0]["prompt"] == "prompt"
    assert log_messages[0]["response"]["q"] == "question"
    assert log_messages[1]["prompt"] == "prompt2"


def test_get_log_messages_skips_control_messages() -> None:
    """It skips envelopes other than DATA_MESSAGEs."""
    not_data = {**_data_message(_search_record("not data")), "messageType": "CONTROL_MESSAGE"}
    logs = [CONTROL_MESSAGE, not_data, _data_message(_search_record("q1"))]

    log_messages = rank_eval_utils.get_log_messages(logs, "search")

    assert _queries(log_messages) == ["q1"]


def test_get_log_messages_skips_events_that_are_not_json_objects() -> None:
    """It skips log events whose message isn't a JSON object."""
    log = _data_message(
        "START RequestId: 0b6a1f3e-1d7c-4c1e-9a49-6f1d5c2b7e10 Version: $LATEST\n",
        _search_record("q1"),
        "42",
        json.dumps({"_aws": {"Timestamp": 1760378400000, "CloudWatchMetrics": []}, "search_answer_length": 512}),
        json.dumps({"name": "server.main", "message": "Query response"}),
        _search_record("q2") + "\n",
    )

    log_messages = rank_eval_utils.get_log_messages([log], "search")

    assert _queries(log_messages) == ["q1", "q2"]


def test_load_logs_reads_gzip_and_plain_objects(s3: Stubber) -> None:
    """It reads gzip and plain objects holding several envelopes, whatever their ContentType."""
    first, second, third = (_data_message(_search_record(q)) for q in ["q1", "q2", "q3"])
    _stub_list_page(s3, ["2026/10/13/18/gzip", "2026/10/13/18/plain"])
    _stub_get_object(s3, "2026/10/13/18/gzip", _firehose_gzip(CONTROL_MESSAGE, first), "binary/octet-stream")
    _stub_get_object(s3, "2026/10/13/18/plain", f" {json.dumps(second)}\n\n{json.dumps(third)}\r\n".encode())

    logs = rank_eval_utils.load_logs(BUCKET)

    assert logs == [CONTROL_MESSAGE, first, second, third]
    assert _queries(rank_eval_utils.get_log_messages(logs, "search")) == ["q1", "q2", "q3"]


def test_load_logs_reads_every_page(s3: Stubber) -> None:
    """It reads the objects on every page of the listing."""
    first, second = (_data_message(_search_record(q)) for q in ["q1", "q2"])
    _stub_list_page(s3, ["2026/10/13/18/a"], prefix="2026/", next_page="page-2")
    _stub_list_page(s3, ["2026/10/13/19/b"], prefix="2026/", page="page-2")
    _stub_get_object(s3, "2026/10/13/18/a", _firehose_gzip(first))
    _stub_get_object(s3, "2026/10/13/19/b", _firehose_gzip(second))

    logs = rank_eval_utils.load_logs(BUCKET, prefix="2026/")

    assert logs == [first, second]


def test_load_logs_without_objects(s3: Stubber) -> None:
    """It returns no envelopes when no object matches the prefix."""
    _stub_list_page(s3, [], prefix="2099/")

    assert rank_eval_utils.load_logs(BUCKET, prefix="2099/") == []


_GZIP_MEMBER = gzip.compress(json.dumps(CONTROL_MESSAGE).encode())


@pytest.mark.parametrize(
    "body",
    [
        pytest.param(b'{"messageType": "DATA_MESSAGE", "logEvents": [', id="truncated-json"),
        pytest.param(b'["not an envelope"]', id="json-array"),
        pytest.param(_GZIP_MEMBER[:-4], id="truncated-gzip"),  # EOFError
        pytest.param(_GZIP_MEMBER[:-8] + bytes(4) + _GZIP_MEMBER[-4:], id="gzip-bad-crc"),  # gzip.BadGzipFile
        pytest.param(_GZIP_MEMBER[:10] + b"\x07" + bytes(16), id="corrupt-deflate"),  # zlib.error
    ],
)
def test_load_logs_names_unreadable_object(s3: Stubber, body: bytes) -> None:
    """It names the object it can't read."""
    _stub_list_page(s3, ["2026/10/13/18/bad"])
    _stub_get_object(s3, "2026/10/13/18/bad", body)

    with pytest.raises(ValueError, match=re.escape(f"s3://{BUCKET}/2026/10/13/18/bad")):
        rank_eval_utils.load_logs(BUCKET)
