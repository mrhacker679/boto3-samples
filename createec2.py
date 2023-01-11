import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Set the name of the key pair
key_pair_name = 'my-key-pair'

# Create a new key pair
key_pair = ec2.create_key_pair(KeyName=key_pair_name)

# Store the key pair's private key
with open(key_pair_name + '.pem', 'w') as key_file:
    key_file.write(key_pair['KeyMaterial'])

# Set the name of the security group
security_group_name = 'my-security-group'

# Create a new security group
security_group = ec2.create_security_group(
    GroupName=security_group_name,
    Description='This is my security group'
)

# Authorize incoming SSH traffic
ec2.authorize_security_group_ingress(
    GroupName=security_group_name,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

# Set the name of the image (AMI)
ami_name = 'ami-0f65671a86f061fcd'

# Set the name of the instance type
instance_type = 't2.micro'

# Set the name of the subnet
subnet_name = 'my-subnet'

# Launch the instance
ec2.run_instances(
    ImageId=ami_name,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    SecurityGroupIds=[security_group_name],
    SubnetId=subnet_name,
    MinCount=1,
    MaxCount=1
)
