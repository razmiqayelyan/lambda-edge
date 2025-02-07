```
# AWS Lambda Basic Auth

## Description
A simple AWS Lambda function that adds **Basic Authentication** for AWS CloudFront requests. It checks the `Authorization` header and blocks unauthorized requests.

## How It Works
1. CloudFront triggers the Lambda function.
2. The function checks for a valid `Authorization` header.
3. If the credentials match, the request proceeds; otherwise, it returns `401 Unauthorized`.

## Setup

### 1. Deploy to AWS Lambda
```
zip lambda_function.zip lambda_function.py
aws lambda create-function --function-name basicAuthLambda \
    --runtime python3.x \
    --role arn:aws:iam::YOUR_AWS_ACCOUNT_ID:role/YOUR_LAMBDA_ROLE \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_function.zip
```
Replace `YOUR_AWS_ACCOUNT_ID` and `YOUR_LAMBDA_ROLE` with actual values.

### 2. Attach to CloudFront
- Go to your CloudFront distribution.
- Add the Lambda function as an **Origin Request** or **Viewer Request** trigger.

### 3. Send Requests with Authentication
Use a valid `Authorization` header:
```
Authorization: Basic YWRtaW46YWRtaW5hZG1pbg==
```
Replace the value with your **Base64-encoded** username and password.

## Notes
- **Use HTTPS** to protect credentials.
- **Don't hardcode passwords** in production (use AWS Secrets Manager).
- **Rotate credentials periodically** for security.

## License
MIT License – Free to use and modify.
```
