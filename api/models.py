import os
import torch
import boto3
from config.settings import MODEL_PATH, AWS_BUCKET_NAME, AWS_MODEL_KEY

def download_model_from_s3():
    """Download model from AWS S3 if AWS credentials exist."""
    if AWS_BUCKET_NAME and not os.path.exists(MODEL_PATH):
        print(f"Downloading model from S3: {AWS_BUCKET_NAME}/{AWS_MODEL_KEY}...")
        s3 = boto3.client("s3")
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        s3.download_file(AWS_BUCKET_NAME, AWS_MODEL_KEY, MODEL_PATH)
        print("Download complete!")

# Use AWS download **only if AWS_BUCKET_NAME is set** (for later)
if AWS_BUCKET_NAME:
    download_model_from_s3()

# Load the model
def load_model():
    model = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
    model.eval()
    return model

model = load_model()
