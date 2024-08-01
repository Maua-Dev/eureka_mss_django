#!/usr/bin/env python3
import os

# from dotenv import load_dotenv

import aws_cdk as cdk

from iac.iac_stack import IacStack

print("Starting the CDK")

app = cdk.App()

# load_dotenv()
aws_region = os.environ.get("AWS_REGION")
aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
stack_name = os.environ.get("STACK_NAME")

github_ref_name = os.environ.get("STAGE")

if 'prod' == github_ref_name:
    stage = 'PROD'

elif 'homolog' == github_ref_name:
    stage = 'HOMOLOG'

elif 'dev' == github_ref_name:
    stage = 'DEV'

else:
    stage = 'TEST'

tags = {
    'project': 'EurekaApi',
    'stage': stage,
    'stack': 'BACK',
    'owner': 'DevCommunity'
}

IacStack(app, stack_name+stage, env=cdk.Environment(account=aws_account_id, region=aws_region), tags=tags)

app.synth()