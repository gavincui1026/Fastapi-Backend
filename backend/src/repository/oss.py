from abc import ABC, abstractmethod

import boto3

from src.config.manager import settings

class OSSRepository(ABC):
    @abstractmethod
    def upload(self, key: str, file: bytes):
        pass
    @abstractmethod
    def download(self, key: str) -> bytes:
        pass
    @abstractmethod
    def delete(self, key: str):
        pass




class AmazonS3Repository(OSSRepository):
    def __init__(self):
        self.bucket = settings.AWS_BUCKET_NAME
        self.client = boto3.client("s3", aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    def upload(self, key: str, file: bytes):
        # 计算文件的MD5值，防止重复上传
        # 文件在oss上的key值采用MD5值
        self.client.put_object(Bucket=self.bucket, Key=key, Body=file)

    def download(self, key: str) -> bytes:
        response = self.client.get_object(Bucket=self.bucket, Key=key)
        return response['Body'].read()

    def delete(self, key: str):
        self.client.delete_object(Bucket=self.bucket, Key=key)

