#! /usr/bin/env python3
#this script sets up temporary AWS MFA credentials for an IAM user 
import os
import subprocess
import json
import configparser
from pathlib import Path
from aws_default_credentials import aws_access_key_id
from aws_default_credentials import aws_secret_access_key

  #mfa code
token = input("enter token_code: ")
  
  #create a json file to capture json credential output 
with open("credential.json", "w") as credential_file:
    subprocess.run(["aws","sts","get-session-token", "--serial-number",
                 "arn:aws:iam::324320755747:mfa/desire.bahbioh.labs", "--token-code", token], 
                 stdout = credential_file)

  #load the json and extract keys as environment variables 
  #to populate the temp profile in ~/.aws/credentials file 
with open("credential.json" , "r") as read_credential_file:
    data = json.load(read_credential_file)

os.environ["TMP_ACCESS_KEYID_ENV"] = (data['Credentials']['AccessKeyId']) 
os.environ["TMP_SECRET_ACCESS_KEY"] = (data['Credentials']['SecretAccessKey']) 
os.environ["TMP_SESSION_TOKEN"] = (data['Credentials']['SessionToken'])

  #parse environment variable values for ".aws/credentials" file which is of type INI 
config = configparser.ConfigParser()

config["default"] = {
    "aws_access_key_id" : aws_access_key_id,
    "aws_secret_access_key" : aws_secret_access_key 
}

config["temp"] = {
    "output" : "json",
    "region" : "us-east-1",
    "aws_access_key_id" : os.environ.get("TMP_ACCESS_KEYID_ENV"), 
    "aws_secret_access_key" : os.environ.get("TMP_SECRET_ACCESS_KEY"), 
    "aws_session_token" : os.environ.get("TMP_SESSION_TOKEN")
  }

#update "credentials" file with new parsed value
homedir = Path.home()
with open (str(homedir)+"/.aws/credentials", "w") as aws_updated_credentials:
  config.write(aws_updated_credentials)
  print("\"temp\" profile successfuly updated in aws credential file!" 
        "\nyou can now use \"--profile temp\" with the aws cli")