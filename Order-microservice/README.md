# Order Service - Serverless with AWS Lambda 



## Overview
This is a serverless microservice built using AWS Lambda (Python), DynamoDB, and SQS. It allows you to create and retrieve product orders using a RESTful API deployed via API Gateway.

## Architecture
![alt text](event-drivendiadream-1.png)
## Technologies Used
- Python 3.9+
- AWS Lambda
- AWS DynamoDB
- Amazon SQS
- API Gateway
- Serverless Framework


## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/order-service.git
   cd order-service
   ```

2. **Install dependencies:**
   ```bash

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



