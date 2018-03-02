"""
Section:
    Reading and Writing

Author:
    Carlos Aguilar (Simon Ward-Jones)

Description:
    Read a file from S3

Tags:
    read, S3, boto3
"""

import boto3
import pickle

bucket         = 'amazon-sagemaker-poc'
region         = boto3.Session().region_name
s3Client       = boto3.client('s3');
bucketList     = s3Client.list_objects_v2(Bucket=bucket);

# To retrieve the full list of keys
bucketContents = [currentKey['Key'] for currentKey in bucketList['Contents']];
print(bucketContents)

# To read an object
keyName  = 'tpsPurchases.pickle'
obj      = s3Client.get_object(Bucket=bucket, Key=keyName)

dfFromPickle = pickle.loads(obj['Body'].read())
print(dfFromPickle.shape)