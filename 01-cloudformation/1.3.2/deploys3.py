#! /usr/bin/env python3
import boto3
import logging
from botocore.exceptions import ClientError
from regionslist import regions

session = boto3.Session(profile_name='temp')


def deployStack(region):
        temp_cfnclient = session.client('cloudformation', region_name=region)
        response = temp_cfnclient.create_stack(
        StackName='desi-stack',
        ResourceTypes=[
            'AWS::*'
        ],
        TemplateURL='https://desire-cfn-templates.s3.amazonaws.com/s3bucket.json'
        )
        if (response):
            print("Stack created successfuly!")


for region in regions:
    try:
         deployStack(region)
    except ClientError as e:
     logging.error(e)



