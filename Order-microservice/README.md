# Order Service - Serverless with AWS Lambda (Python)

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [API Endpoints](#api-endpoints)
6. [Environment Configuration](#environment-configuration)
7. [Deployment](#deployment)
8. [SQS Integration](#sqs-integration)
9. [Permissions & IAM](#permissions--iam)
10. [License](#license)

## Overview
This is a serverless microservice built using AWS Lambda (Python), DynamoDB, and SQS. It allows you to create and retrieve product orders using a RESTful API deployed via API Gateway.

## Architecture
```
Client -> API Gateway -> AWS Lambda -> DynamoDB
                           |
                        (Optional)
                          ↓
                        Amazon SQS
```
> ✅ This architecture decouples order creation and background processing via SQS.

## Technologies Used
- Python 3.9+
- AWS Lambda
- AWS DynamoDB
- Amazon SQS
- API Gateway
- Serverless Framework
- boto3

## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/order-service.git
   cd order-service
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Serverless Framework (if not already):**
   ```bash
   npm install -g serverless
   ```

4. **Deploy to AWS:**
   ```bash
   sls deploy
   ```

## API Endpoints

| Method | Endpoint  | Description        |
|--------|-----------|--------------------|
| POST   | `/orders` | Create a new order |
| GET    | `/orders` | Get all orders     |

## Sample Payload (POST `/orders`)
```json
{
  "product": "Laptop",
  "quantity": 2
}
```

## Environment Configuration
Update `serverless.yml` with your environment variables and IAM permissions.

## Deployment
To deploy the service:
```bash
sls deploy
```

To remove the stack:
```bash
sls remove
```

## SQS Integration
To integrate SQS into the workflow:

- Create an SQS queue via the AWS console or `serverless.yml`.
- Add permissions for `sqs:SendMessage`, `sqs:ReceiveMessage`.
- Modify `createOrder` function to publish order data to the SQS queue instead of DynamoDB (or in addition to it).

## Permissions & IAM
Your Lambda functions need the following IAM permissions:
```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:PutItem",
    "dynamodb:Scan",
    "sqs:SendMessage"
  ],
  "Resource": "*"
}
```
> Note: Replace `*` with specific resource ARNs in production.

## License
MIT License

