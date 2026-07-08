import os
import random
import uuid
from pathlib import Path

import boto3


def main() -> None:
    bucket_name = os.getenv("BUCKET_NAME", f"python-s3-demo-{uuid.uuid4().hex[:8]}")
    region = os.getenv("AWS_REGION", "ca-central-1")

    s3 = boto3.client("s3", region_name=region)

    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region}
        if region != "us-east-1"
        else None,
    )

    number_of_files = 1 + random.randint(0, 5)
    print(f"number_of_files: {number_of_files}")

    for i in range(number_of_files):
        print(f"i: {i}")
        filename = f"file_{i}.txt"
        output_path = Path("/tmp") / filename
        output_path.write_text(str(uuid.uuid4()))
        s3.put_object(Bucket=bucket_name, Key=filename, Body=output_path.read_bytes())


if __name__ == "__main__":
    main()
