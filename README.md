# 🧠 AWS Serverless Image Recognition App

This is a fully serverless AWS project that uses Amazon Rekognition to detect labels in images uploaded to an S3 bucket. The solution is built with S3,Lambda (Python), API Gateway, IAM, and CloudWatch.

---

## 📸 How It Works

1. You upload an image to an S3 bucket.
2. The upload triggers a Lambda function via an S3 event notification.
3. The Lambda function uses Amazon Rekognition to detect labels in the image.
4. The labels are logged to CloudWatch.

---

## 🛠️ Architecture
---

## 🔧 Tech Stack

- **AWS Lambda** (Python 3.13)
- **Amazon Rekognition**
- **Amazon S3**
- **Amazon CloudWatch**
- **IAM Roles**
- **Python `boto3` SDK**

---

## 🚀 Deployment Steps

> ⚠️ Assumes you have AWS CLI and credentials configured.

1. **Create the S3 Bucket**
   - Name: `image-upload-giles-2025` (or your own)
   - Enable event notifications to trigger Lambda on `ObjectCreated:Put`

2. **Create the Lambda Function**
   - Runtime: Python 3.13
   - Add environment variable: `REKOGNITION_REGION=eu-west-1`
   - Use the provided `lambda_function.py` (below)

3. **IAM Role for Lambda**
   - Grant permissions:  
     - `AmazonRekognitionFullAccess`
     - `AmazonS3ReadOnlyAccess`
     - `CloudWatchLogsFullAccess`

4. **Upload a Test Image**
   - Upload `Cat01.jpg` to your S3 bucket

5. **Check CloudWatch Logs**
   - See label output like: `Labels detected: Cat, Animal, Pet`

---

## 🧪 Sample Event File

`test-event.json` for testing manually from Lambda console:

```json
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "image-upload-giles-2025"
        },
        "object": {
          "key": "Cat01.jpg"
        }
      }
    }
  ]
}
