import boto3

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Use the filter() method of the images collection to retrieve all Windows-based images
response = ec2.describe_images(Filters=[{'Name': 'architecture', 'Values': ['x86_64']},
                                        {'Name': 'virtualization-type', 'Values': ['hvm']},
                                        {'Name': 'root-device-type', 'Values': ['ebs']},
                                        {'Name': 'state', 'Values': ['available']}
                                       ])

# Print the ID and name of each image
for image in response['Images']:
    print(image['ImageId'], image['Name'])
