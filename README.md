# DBR-on-AWS-lambda
Learn dynamsoft barcode reader in AWS lambda with python through aws cli and serverless framework cli.
## environment & prerequisites:
1. python: 3.9
2. lambda function: x86_64
3. [create IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
4. [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
5. newer version of [serverless framework cli](https://www.serverless.com/framework/docs/providers/aws/cli-reference) is prefered

## Dynamsoft barcode reader version:
dbr: [9.6.20](https://pypi.org/project/dbr/#files)

## RUN the example with ServerlessFramework cli
1. 
configure aws credentials
```
aws configure
```
2. 
modify `aws region` and your `profile`(aws credential) in `serverless.yml`
```
#change aws region here
region: ap-east-1
# change your credential profile here
# if you are using aws cli the first time, the profile should be 'default'.
# (on mac) find all your profiles in ~/.aws/credentials
profile: ServerlessFrameworkUser
```
3. 
deploy to aws lambda
```
sls deploy
```
You can see the function is created on [lambda](https://ap-east-1.console.aws.amazon.com/lambda/home?region=ap-east-1#/functions/dbr-tester-dev-hello?tab=code) in **your aws region**.


4. 
add dbr dependency layer

go to [lambda](https://ap-east-1.console.aws.amazon.com/lambda/home?region=ap-east-1#/functions/dbr-tester-dev-hello?tab=code) in **your aws region** -> AWS Lambda -> Layers -> Create layer

configure the layer and upload `/layers/dbr@9.6.20/python.zip`
![create DBR layer](https://tst.dynamsoft.com/team/ethan/github/create_layer.jpg)

5. 
After the layer is created, please go to `dbr-tester-dev-hello` function. Then add DBR layer as a Custom layer.
![add DBR layer](https://tst.dynamsoft.com/team/ethan/github/add_layer.jpg)


6. 
test the lambda function:
```
sls invoke -f hello
```
expected tesult:
```
[
    "dynamsoft is awesome"
]
```

## Run the example using the AWS console
1. 
add dbr dependency layer: 
go to [lambda](https://ap-east-1.console.aws.amazon.com/lambda/home?region=ap-east-1#/functions/dbr-tester-dev-hello?tab=code) in **your aws region** -> AWS Lambda -> Layers -> Create layer

configure the layer and upload the `python.zip` file from `/layers/dbr@9.6.20/python.zip`
![create DBR layer](https://tst.dynamsoft.com/team/ethan/github/create_layer.jpg)

2. 
create lambda function
copy the code from /handler.py into your function

3. 
Then add Custom layer.
![add DBR layer](https://tst.dynamsoft.com/team/ethan/github/add_layer.jpg)

4. 
run test 
expected test result:
```
[
  "dynamsoft is awesome"
]
```