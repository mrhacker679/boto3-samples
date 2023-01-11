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