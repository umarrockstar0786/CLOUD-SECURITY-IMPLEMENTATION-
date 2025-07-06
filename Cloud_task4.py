// least-privileged policy for Lambda to S3 read + DynamoDB write
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadConfig",
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-config-bucket/config/*"]
    },
    {
      "Sid": "AllowDynamoDBWrite",
      "Effect": "Allow",
      "Action": ["dynamodb:PutItem"],
      "Resource": ["arn:aws:dynamodb:us-east-1:123456789012:table/MyTable"]
    },
    {
      "Sid": "EnforceTLS",
      "Effect": "Deny",
      "NotAction": "iam:*",
      "Resource": "*",
      "Condition": {"Bool": {"aws:SecureTransport": "false"}}
    }
  ]
}
