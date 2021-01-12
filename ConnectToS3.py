import boto3
import os
from CredentialsApi import access_key, secret_access_key

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

for file in os.listdir():
    try:
        upload_file_bucket = 'trial-mapillary'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)
        message = "Success"
    except Exception as e:
        message = "Error ocurred"
        print(message)