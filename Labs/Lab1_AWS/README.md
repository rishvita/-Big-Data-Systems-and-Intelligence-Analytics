# AWS

### [CLAAT document](https://codelabs-preview.appspot.com/?file_id=11xKKxXM-ssWfJCw5J8FfJ4zEU-1T78Hw5rMuj7ZBaP4#0)

### Setup

#### AWS Signup & Configuration 

Sign up for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start). Additonally, the AWS Command Line Interface is required to interact with AWS Services. Download AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)


#### Configuring your AWS CLI 

Download your AWS Access and Secret access keys for your AWS Account. Steps to generate and download your keys can be found [here](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/id_credentials_access-keys.html) 


:warning: Never share your access and secret access keys or push them to GitHub<br />


Open command line tool of choice on your machine and run `aws configure`. Enter your access and secret access keys and leave the default region name and output format as null. 

```
$ aws configure
AWS Access Key ID [None]: ''
AWS Secret Access Key [None]: ''
Default region name [None]: 
Default output format [None]: json
```

#### Billing Alerts

Set up billing alerts for your AWS Account [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

### Getting Started with AWS

#### Requirements

```
pip3 install Faker
pip3 install boto3
pip install lambda 
```


### Build + Deploy Lambda
Lambda functions only contain a basic installation of Python + boto3 and do not contain any external libraries. Any external libraries need to be packaged and deployed to AWS.

#### Building the Lambda
We'll make use for virtualenv to create a virtual environment. For correct virtualenv setup and configuration, refer this documentation

#### Create a Virtual Environment

mkdir first-lambda
cd first-lambda
mkvirtualenv first_lambda
pip3 install python-lambda

If your python script requires any additonal libraries - you may install it at this stage.

#### Initiate Lambda Deployement

#### lambda init

This creates the following files: event.json, __init__.py, service.py, and config.yaml.
The service.py is the file we are interested in. Edit service.py with your Python code and we are good to go.

#### Configuring the Lambda

config.yaml file contains configuration information required to deploy the Lambda package to AWS. Configure the file with your access keys, secret access keys and function name before packaging and deploying the Python code. An example is as follows

region: us-east-1
function_name: my_lambda_function
handler: service.handler
description: My first lambda function
runtime: python3.7
role: lambda_basic_execution

> :Note: if access key and secret are left blank, boto will use the credential defined in the [default] section of ~/.aws/credentials.
aws_access_key_id: <Enter your Access Keys>
aws_secret_access_key: <Enter your Secret Access Keys>

These may be changed based on how much memory your code needs
timeout: 15
memory_size: 512

Experimental Environment variables

Build options
build:
  source_directories: lib
  
#### Deploying the Lambda Function
Although - you could zip the contents of the directory and upload the file to the Lambda console - let's take advantage of python-lambda to do it for us

#### lambda deploy
This should create a new Lambda function on your AWS Lambda Console

#### Contents

- `s3_upload.py` - Python script to generate some fake data using Faker and upload to your S3 Bucket 
- `s3_download.py` - Download the file of your choice from S3 to your local environemnt 
- `comprehend_demo.py` - Use AWS Comprehend to detect sentiment and extract PII features from your data. Additonal APIs can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html)
- Lambda Functions - Deploying Lambda functions using Python Lambda. 


