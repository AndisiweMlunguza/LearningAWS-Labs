# Serverless REST API using AWS Lambda + API Gateway + DynamoDB

This project is a fully serverless REST API built on AWS using:
- **Lambda** for backend logic (Python)
- **API Gateway (HTTP API)** for routing requests
-  **DynamoDB** for persistent storage
-  **IAM** for access control

## Features

- `POST /Items`: Create a new item (`name`, `price`)
- `GET /Items`: Retrieve all items from the table

##  Setup Guide

1. **Create DynamoDB Table**
   - Name: `Items`
   - Primary key: `id` (string)

2. **Deploy Lambda Function**
   - Use Python 3.12 runtime
   - Attach IAM role with `dynamodb:PutItem`, `dynamodb:Scan`

3. **Configure API Gateway**
   - Use **HTTP API** (not REST API)
   - Routes:
     - `POST /Items`
     - `GET /Items`
   - Integrate each route with the Lambda function

4. **Enable CORS (Optional)** if using from frontend

## Example cURL Commands
### POST
```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/Items \
-H "Content-Type: application/json" \
-d '{"name":"Book", "price":10}'
GET
bash
CopyEdit
curl https://<api-id>.execute-api.<region>.amazonaws.com/Items
 Testing Tips
•	Use CloudWatch Logs for debugging errors like KeyError: 'httpMethod' — HTTP APIs use event['requestContext']['http']['method'].
•	Set log retention to 1 week to avoid charges.
 Lessons Learned
•	Difference between REST API vs HTTP API in API Gateway
•	IAM policy setup for DynamoDB access
•	Debugging Internal Server Error responses with logs
•	Understanding API Gateway → Lambda event structure
