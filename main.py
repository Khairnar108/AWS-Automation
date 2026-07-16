import boto3

# IAM
iam = boto3.client("iam")

user = iam.create_user(
    UserName="DeveloperUser2"
)

print("IAM User Created")

# S3
s3 = boto3.client("s3")

bucket = "aniket-project-demo-123456"

s3.create_bucket(
    Bucket=bucket,
    CreateBucketConfiguration={
        "LocationConstraint":"ap-south-1"
    }
)

print("Bucket Created")

# EC2
ec2 = boto3.resource("ec2")

instance = ec2.create_instances(
    ImageId="ami-xxxxxxxx",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro"
)

print("EC2 Instance Created")

print(instance[0].id)