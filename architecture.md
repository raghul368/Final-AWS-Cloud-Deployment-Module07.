# AWS Architecture

```text
User / Browser
     |
     +----> Amazon S3 (static website files)
     |
     +----> Amazon API Gateway (HTTP API)
                    |
                    v
              AWS Lambda
                    |
                    v
             Amazon CloudWatch
```

## Services
- **Amazon S3:** stores and serves static website assets.
- **Amazon API Gateway:** exposes an HTTP endpoint for backend requests.
- **AWS Lambda:** runs the Python API handler.
- **AWS IAM:** grants the required service permissions using least privilege.
- **Amazon CloudWatch:** stores Lambda logs and supports monitoring.

The browser can load the static site from S3 and call the API Gateway endpoint separately. Configure CORS on API Gateway for the website's actual origin before connecting them.
