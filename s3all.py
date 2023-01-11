#######  FOR CREATING S# BUCKET ###################

#!/usr/bin/python3
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket = 'mybucket-123')



######## LISTING S3 BUCKETS ####################

#!/usr/bin/python3
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response['Buckets'])


################ UPLOADING OBJECTS TO S3 ######################
#!/usr/bin/python3
import boto3, glob

s3 = boto3.client('s3')

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    response = s3.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    return response


upload_files('data/file1.txt', 'mybucket-123')  # FOR UPLOADING SINGLE OBEJCT



################# Another example with little modification #####################

#!/usr/bin/python3

import boto3, glob

s3 = boto3.client('s3')
bucket = 'mybucket-123'

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    response = s3.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(response)

# UPLOADING MULTIPLE OBJECTS THROUGH FOR LOOP
args = {'ACL': 'public-read'}  # FOR ASSIGN PUBLIC READ ACCESS
files = glob.glob('data/*')
for file in files:
    upload_files(file, bucket)
    print('Uploaded', file)
    
    
 ############# Downloading the files from s3 ###################

import boto3
s3 = boto3.client('s3')
list(s3.buckets.all())       #USED TO GET NAMES OF THE EXISTING BUCKETS

# YOU NEED TO CHOSE A BUCKET
bucket = s3.Bucket('mybucket-123')
files = list(bucket.objects.all())

for file in files:
   s3.download_file('mybucket-123', file.key, 'path_to_download') 
    
    
#################################################
import boto3

# create an S3 client
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# specify the bucket and file you want to download
bucket_name = 'mybucket-123'
file_name = 'example.txt'

# download the file
s3.download_file(bucket_name, file_name, '/path/to/local/file')

###########################################################

import boto3

# create an S3 resource
s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# specify the bucket and file you want to download
bucket_name = 'mybucket-123'
file_name = 'example.txt'

# download the file
s3.Bucket(bucket_name).download_file(file_name, '/path/to/local/file')

###############################################################


###################### ADDING POLICY TO BUCKET ##################################

import json, boto3

s3 = boto3.client('s3')

bucket_name = 'mybukcet-123'
bucket_policy = {
   "Version":"2012-10-17",
   "Statement":[
     {
       "Sid":"PolicyForAllowUploadWithACL",
       "Effect":"Allow",
       "Principal": "*",
       "Action":["s3:GetObject","s3:GetObjectVersion"],
       "Resource":"arn:aws:s3:::mybucket-123/*",
     }
   ]
}
    
bucket_policy = json.dumps(bucket_ploicy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy) 


#############################################################################

######################### TO GET THE BUCKET POLICY #########################

import boto3

s3 = boto3.client('s3')
policy = s3.get_bucket_policy('mybucket-123')
print(policy)

############################################################################

######################### STATIC WEB SITE HOSTING ##########################

import boto3

s3 = boto3.client('s3')
bucket_name = 'mybucket-123'
conf = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'}
}

s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=conf)

args = {'ACL': 'public-read', 'ContentType': 'text/html'}
upload_files('data/index.html', bucket_name, object_name='index.html', args=args)
    
###########################################################################



