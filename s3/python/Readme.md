# Python S3 bucket project

This folder now contains a simple Python package for working with S3 buckets.

## Install

From this directory, run:

```bash
python -m pip install -e .
```

## Usage

Run the Ruby-like example:

```bash
python -m s3_bucket_demo.example
```

List buckets:

```bash
s3-bucket-demo --action list
```

Create a bucket:

```bash
s3-bucket-demo --action create --bucket my-example-bucket --region us-east-1
```

Upload a file:

```bash
s3-bucket-demo --action upload --bucket my-example-bucket --key hello.txt --file /tmp/hello.txt --region us-east-1
```

Delete a bucket:

```bash
s3-bucket-demo --action delete --bucket my-example-bucket --region us-east-1
```
