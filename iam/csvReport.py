import boto3
import csv
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_expired_access_keys(age_threshold):
    # Connect to the IAM client
    iam = boto3.client('iam')
    
    expired_keys = []
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
                # Append the user name and age of the access key
                expired_keys.append([user['UserName'], age])
    return expired_keys


def generate_csv_report(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['UserName', 'Access Key Age (days)'])
        writer.writerows(data)


def send_email(to, subject, body, filename):
    msg = MIMEMultipart()
    msg['From'] = 'Sender Email address'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    with open(filename, 'rb') as f:
        attachment = MIMEText(f.read(), 'csv')
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Sender Email Address', 'Email password')
    server.send_message(msg)
    server.quit()
