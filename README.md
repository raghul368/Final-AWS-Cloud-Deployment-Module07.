# Module 07 – Final AWS Cloud Deployment Project

A starter project for the AWS Cloud & DevOps internship at Codomax Digital Solutions.

## Project structure

- `website/index.html` — responsive project overview website.
- `lambda/lambda_function.py` — sample Python Lambda handler for API Gateway.
- `docs/architecture.md` — AWS architecture and service explanation.

## AWS services covered

1. **Amazon S3** — static website file storage/hosting.
2. **Amazon API Gateway** — HTTP API endpoint.
3. **AWS Lambda** — serverless backend execution.
4. **AWS IAM** — roles and least-privilege permissions.
5. **Amazon CloudWatch** — logs and monitoring.

## Deployment outline

### Frontend (S3)
1. Create an S3 bucket in your AWS account.
2. Upload the contents of the `website` folder.
3. Configure an appropriate static website hosting solution. For production, consider CloudFront with a private S3 origin rather than making the bucket public.
4. Open the website endpoint or CloudFront URL and test it.

### Backend (Lambda + API Gateway)
1. Create a Lambda function with a supported Python runtime.
2. Copy the code from `lambda/lambda_function.py` into the Lambda editor.
3. Deploy and test the function.
4. Create an HTTP API in API Gateway and add a Lambda integration.
5. Create a route such as `GET /hello`, then deploy the API.
6. Configure CORS for the exact frontend origin if the website calls the API.
7. Test the API invoke URL.

### Security and monitoring
- Use an IAM execution role with only the permissions the function needs.
- Keep S3 Block Public Access enabled unless your chosen hosting design specifically requires otherwise.
- Never commit AWS access keys, passwords, or other secrets.
- Review Lambda logs and metrics in Amazon CloudWatch.
- Check AWS pricing before creating resources.

## Important
This repository is a learning starter project. It does not provision AWS resources or provide a deployed live endpoint automatically. Follow the AWS console steps in your own account and verify the configuration before sharing the site.
