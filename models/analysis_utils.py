"""Utility functions for analyzing logs."""

import gzip
import json
import re
from io import BytesIO
from typing import Any

import boto3  # type: ignore
from tqdm import tqdm


def load_logs(bucket_name: str, prefix: str = "") -> list[dict[str, Any]]:
    """Load logs from S3 bucket."""
    # Initialize an empty list to hold the JSON objects
    json_objects = []

    # Create an S3 client
    s3 = boto3.client("s3")

    # Get a list of all the objects in the bucket with the specified prefix
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)["Contents"]

    # Iterate over each object in the bucket
    for obj in tqdm(objects):
        # Download the object
        file_obj = s3.get_object(Bucket=bucket_name, Key=obj["Key"])

        # Check if the file is gzipped
        if file_obj["ContentType"] in ["application/octet-stream", "application/x-gzip"]:
            # Unzip the file
            gzip_file = gzip.GzipFile(fileobj=BytesIO(file_obj["Body"].read()))
            file_content = gzip_file.read().decode("utf-8")
        else:
            # Read the file content as plain text
            file_content = file_obj["Body"].read().decode("utf-8")

        # Parse the file content as JSON
        # first, split separate JSON objects by adding a newline character
        file_content = re.sub(r"}{\"(?![,}])", '}\n{"', file_content, flags=re.UNICODE)
        # then parse each line as a JSON object
        for line in file_content.split("\n"):
            json_obj = json.loads(line)

            # Add the JSON object to the list
            json_objects.append(json_obj)

    return json_objects


def get_log_messages(logs: list[dict[str, Any]], message_type: str) -> list[dict[str, Any]]:
    """Get log messages of a specific type."""
    messages = []
    for log in logs:
        if "logEvents" not in log:
            continue
        for log_event in log["logEvents"]:
            if "message" not in log_event:
                continue
            message = json.loads(log_event["message"])
            if "message" not in message or message["message"] != message_type:
                continue
            messages.append(message)
    return messages
