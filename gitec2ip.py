import boto3

# Create a boto3 client for EC2
ec2 = boto3.client('ec2')

# Retrieve a list of all running instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Create a new empty list to store the IP addresses
ip_addresses = []

# Iterate through the instances and add their IP addresses to the list
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        ip_addresses.append(instance["PrivateIpAddress"])

# Write the list of IP addresses to a file
with open('inventory.txt', 'w') as inventory_file:
    for ip in ip_addresses:
        inventory_file.write(ip + '\n')
