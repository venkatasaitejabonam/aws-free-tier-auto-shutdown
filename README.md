# AWS Free Tier Auto-Shutdown Project

Automatically detect AWS usage costs and immediately stop or delete services to ensure no bill is generated, staying strictly within the AWS Free Tier.

## Features
- AWS Budgets with a $0.01 threshold
- SNS notifications
- Lambda cleanup function to stop/delete EC2, Lambda, DynamoDB, API Gateway, and S3
- Optional hourly cleanup using EventBridge
