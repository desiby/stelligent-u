#!/bin/zsh

aws cloudformation create-stack --stack-name desi-ec2s --template-body file://launch.yaml
aws cloudformation wait stack-create-complete --stack-name desi-ec2s
echo "Stack Created! the script will now exit."