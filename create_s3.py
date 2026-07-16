import boto3

s3 = boto3.client("s3")

bucket_name = "aniket-auto-project-12345"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "ap-south-1"
    }
)

print("Bucket Created")
print(bucket_name)