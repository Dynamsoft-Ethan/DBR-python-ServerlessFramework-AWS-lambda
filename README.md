# DBR-on-AWS-lambda
Learn how to use dynamsoft barcode reader on AWS lambda
## sample environment:
python: 3.9\n
lambda function: x86_64\n
aws-cli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html\n
serverless framework cli: https://www.serverless.com/framework/docs/providers/aws/cli-reference\n

## Dynamsoft barcode reader version:
dbr: 9.6.20

## RUN the sample
1. configure aws credentials
```
aws configure
```
2. modify aws region and your profile(aws credential) in `serverless.yml`
```
#change aws region here
region: ap-east-1
# change your credential profile here
# if you are using aws cli the first time, the profile should be 'default'.
# (on mac) find all your profiles in ~/.aws/credentials
profile: ServerlessFrameworkUser
```
3. deploy to aws lambda
```
sls deploy
```
4. Try lambda function:
```
sls invoke -f hello
```
Result:
```
[
    "dynamsoft is awesome"
]
```
