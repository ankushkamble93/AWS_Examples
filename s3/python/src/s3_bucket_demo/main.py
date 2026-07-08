import argparse
import os

from .s3_ops import create_bucket, delete_bucket, list_buckets, upload_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage S3 buckets with Python")
    parser.add_argument("--action", choices=["create", "list", "upload", "delete"], required=True)
    parser.add_argument("--bucket", help="Name of the S3 bucket")
    parser.add_argument("--key", help="Object key for upload")
    parser.add_argument("--file", help="Local file path for upload")
    parser.add_argument("--region", default=os.getenv("AWS_REGION", "us-east-1"), help="AWS region")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.action == "list":
        print(list_buckets())
        return

    if not args.bucket:
        parser.error("--bucket is required for this action")

    if args.action == "create":
        response = create_bucket(args.bucket, args.region)
        print(response)
        return

    if args.action == "upload":
        if not args.key or not args.file:
            parser.error("--key and --file are required for upload")
        response = upload_file(args.bucket, args.key, args.file, args.region)
        print(response)
        return

    if args.action == "delete":
        response = delete_bucket(args.bucket, args.region)
        print(response)


if __name__ == "__main__":
    main()
