
# S3

## setup the shell
you can also put this line inside the profile.ps1(windows)=.bashrc(linux) file 
```
> $ENV:AWS_PROFILE="mohammed"
```
## create bucket
```
> aws s3api  create-bucket --bucket my-test-udacity-bucket --acl public-read-write --region us-east-1 
```

## put object in bucket
```
> aws s3api put-object --bucket my-test-udacity-bucket --key sample.html --body sample.html
```
## s3 buckets remove items and buckets
```
> aws s3api delete-object --bucket my-test-udacity-bucket --key sample.html
> aws s3api delete-object --bucket my-test-udacity-bucket --key index.html
> aws s3api delete-bucket --bucket my-test-udacity-bucket 


```
## s3 buckets remove items and buckets
```
> aws sts get-caller-identity
{
    "UserId": "UserId",
    "Account": "Account",
    "Arn": "arn:aws:iam::Account:user/mohammed"
}

```
## create a role
```
> aws iam create-role --role-name UdacityFlaskDeployCBKubectlRole --assume-role-policy-document file://trust.json --output text --query 'Role.Arn'

```

## create cluster from config file
```
> eksctl create cluster -f cluster.yml  
> eksctl create cluster --region=us-east-1 --zones=us-east-1a,us-east-1b,us-east-1d.
```

## create vpc
```
>  aws cloudformation create-stack --stack-name myFirstStack --region us-east-1 --template-body file://myfirsttemplate.yml
> aws cloudformation describe-stacks
> aws ec2 describe-vpcs
```