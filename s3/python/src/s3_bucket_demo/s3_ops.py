import os
from typing import List

import boto3
from botocore.exceptions import ClientError


def get_s3_client(region_name: str | None = None):
    return boto3.client("s3", region_name=region_name or os.getenv("AWS_REGION", "us-east-1"))


def create_bucket(bucket_name: str, region_name: str | None = None) -> dict:
    s3 = get_s3_client(region_name)
    params = {"Bucket": bucket_name}
    if region_name and region_name != "us-east-1":
        params["CreateBucketConfiguration"] = {"LocationConstraint": region_name}

    response = s3.create_bucket(**params)
    return response


def list_buckets() -> List[str]:
    s3 = get_s3_client()
    response = s3.list_buckets()
    return [bucket["Name"] for bucket in response.get("Buckets", [])]


def upload_file(bucket_name: str, key: str, file_path: str, region_name: str | None = None) -> dict:
    s3 = get_s3_client(region_name)
    with open(file_path, "rb") as fh:
        return s3.put_object(Bucket=bucket_name, Key=key, Body=fh)


def delete_bucket(bucket_name: str, region_name: str | None = None) -> dict:
    s3 = get_s3_client(region_name)
    return s3.delete_bucket(Bucket=bucket_name)
