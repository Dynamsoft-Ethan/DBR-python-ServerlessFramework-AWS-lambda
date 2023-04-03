# DBR-on-AWS-lambda
Learn how to use dynamsoft barcode reader on AWS lambda
## sample environment:
1. python: 3.9
2. lambda function: x86_64
3. [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
4. newer version of [serverless framework cli](https://www.serverless.com/framework/docs/providers/aws/cli-reference) is prefered

## Dynamsoft barcode reader version:
dbr: 9.6.20

## RUN the sample
1. configure aws credentials
```
aws configure
```
2. modify `aws region` and your `profile`(aws credential) in `serverless.yml`
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
You can see the function is created on [lambda](https://ap-east-1.console.aws.amazon.com/lambda/home?region=ap-east-1#/functions/dbr-tester-dev-hello?tab=code) in **your aws region**
4. add dbr dependency layer: 
go to [lambda](https://ap-east-1.console.aws.amazon.com/lambda/home?region=ap-east-1#/functions/dbr-tester-dev-hello?tab=code) in **your aws region** -> AWS Lambda -> Layers -> Create layer

configure the layer and upload the `python.zip` file from `/layers/dbr@9.6.20/python.zip`
![create DBR layer](https://tst.dynamsoft.com/team/ethan/github/create_layer.jpg)

After the layer is created, please go to `dbr-tester-dev-hello` function. Then add Custom layer.
![add DBR layer](https://tst.dynamsoft.com/team/ethan/github/add_layer.jpg)


5. Test lambda function 
Click test on Lambda function console
or
test lambda function through sls cli:
```
sls invoke -f hello
```
6. Result:
```
[
    "dynamsoft is awesome"
]
```
