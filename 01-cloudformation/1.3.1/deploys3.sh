#!/bin/zsh

arrRegions=("$(cat param.json | jq -r '.[0] | .region')" 
            "$(cat param.json | jq -r '.[1] | .region')" 
            "$(cat param.json | jq -r '.[2] | .region')" 
            "$(cat param.json | jq -r '.[3] | .region')")

for i in "${arrRegions[@]}"; do
   aws cloudformation create-stack --stack-name desi-stack --region "$i" --template-body file://s3bucket.yaml
done