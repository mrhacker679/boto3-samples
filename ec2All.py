################ CREATING A KEY PAIR ##########################

import boto3

ec2 = boto3.client('ec2')
key_pair = ec2.create_key_pair(KeyName='mykey123')

with open('mykey123.pem', 'w') as key:
    key.write(key_pair['KeyMaterial'])

################################################################

################## SECURITY GROUPS #############################

import boto3 

ec2 = boto3.client('ec2')
security_groups = ec2.describe_securiy_groups()
print(security_groups)

new = ec2.create_security_groups(
    GroupName = 'mysecgroup',
    Description = 'mysecgroup sg',
    VpcID = 'default'
)

# Now Adding the Inbound rules
gid = new['GroupID']
ec2.authorize_security_group_ingress(
    GroupID = gid,
    IpPermissions = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)


############# CREATING EC2 INSTANCE ##############################

import boto3

ec2_resource = boto3.client('ec2')
instances = ec2_resource.create_instances(
    ImageId = 'ami-02354e95b39ca8dec',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'mykey-123'
    BlockDeviceMappings = [
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True
                'VolumeSize': 20
            }
        }
    ],
    SecurityGroups = ['mysecuritygroup']
)


##################### Start or Stop EC2 Instance #########################

#!/usr/bin/python3
import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Set the ID of the instance
instance_id = 'i-01234567890abcdef0'

# Start the instance
ec2.start_instances(InstanceIds=[instance_id])

# Stop the instance
ec2.stop_instances(InstanceIds=[instance_id])


#################### DELETE EC2 ########################################

import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Set the ID of the instance
instance_id = 'i-01234567890abcdef0'

# Terminate the instance
ec2.terminate_instances(InstanceIds=[instance_id])



################## Get All EC2 ##############################

import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get information about all instances
response = ec2.describe_instances()

# Iterate through the instances
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # Print the instance ID
        print(instance["InstanceId"])
        # Print the instance type
        print(instance["InstanceType"])
        # Print the instance state
        print(instance["State"]["Name"])
