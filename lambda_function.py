import json

def lambda_handler(event, context):
    """Sample Lambda handler for an API Gateway HTTP API integration."""
    body = {
        "project": "Final AWS Cloud Deployment Project",
        "message": "Hello from the AWS serverless backend!",
        "status": "success"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
