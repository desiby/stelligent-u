#! /usr/bin/env python3
import sys
sys.path.insert(1,"/Users/dezbill/stelligent-u/01-cloudformation/1.3.2")
import boto3
import logging
from botocore.exceptions import ClientError
from regionslist import regions

session = boto3.Session(profile_name='temp')


def deleteStack(region):
        temp_cfnclient = session.client('cloudformation', region_name=region)
        response = temp_cfnclient.delete_stack(
        StackName='desi-stack'
        )
        if (response):
            print("Stack deleted successfuly!")


for region in regions:
    try:
         deleteStack(region)
    except ClientError as e:
     logging.error(e)