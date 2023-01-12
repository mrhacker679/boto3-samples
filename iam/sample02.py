import boto3

iam = boto3.client('iam')
users = iam.list_users()
for user in users['Users']:
    username = user['UserName']
    