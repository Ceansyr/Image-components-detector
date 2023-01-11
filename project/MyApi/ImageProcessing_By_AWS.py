import boto3
import requests


def ObjectDetection(imagePath, Service):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    print(Service)


image = open(imagePath, "rb").read()
ObjectDetection(image, "Object Detection")
