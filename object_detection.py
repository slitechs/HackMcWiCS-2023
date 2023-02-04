# Object detection in an image.

# To send HTTP requests.
import requests, os

API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-101"
headers = {"Authorization": os.environ['ODTOKEN']}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()