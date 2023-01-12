# Get the userr and their access key which are older than 25 days

import boto3
from datetime import datetime, timedelta

# Connect to the IAM client
iam = boto3.client('iam')

# Set the age threshold (in days)
age_threshold = 25

# Get a list of all users
users = iam.list_users()['Users']

# Iterate through the users
for user in users:
    # Get the user's access keys
    access_keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
    
    # Iterate through the access keys
    for access_key in access_keys:
        # Get the access key creation date
        create_date = access_key['CreateDate']
        
        # Calculate the age of the access key (in days)
        age = (datetime.now() - create_date).days
        
        # Check if the access key is older than the age threshold
        if age > age_threshold:
            # Print the user name and age of the access key
            print(f"User: {user['UserName']}, Access Key Age: {age} days")
