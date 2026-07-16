import boto3

ec2 = boto3.resource("ec2")

instances = ec2.create_instances(
    ImageId="ami-0b910d1016287a5e7",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro"
)

print("Instance Created")

print(instances[0].id)