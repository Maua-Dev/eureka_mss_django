import boto3
import base64
import datetime
from typing import Optional, Dict

from app.environments import Environments

class S3Manager:
    def __init__(self):
        self.envs = Environments.get_envs()
        stage = self.envs.stage
        if stage == "TEST" or stage == "DEV":
            self.s3 = boto3.client(
                "s3",
                **self.envs.s3_localstack,
            )
        else:
            self.s3 = boto3.client("s3")
        
        def upload_file(self, file_base64: str, key: str, metadata: dict) -> None:
            """
            Upload a file to an S3 bucket
            
            params:
            :param file_base64: base64 encoded file
            :param key: key to store the file in the bucket
            """

            file_body = file_base64.split(",")[1]
            file_content_type = file_base64.split(":")[1].split(";")[0]

            self.s3.put_object(
                Bucket=self.envs.s3_bucket_name,
                Key=key, 
                Body=base64.b64decode(file_body),
                ContentType=file_content_type,
                Metadata={
                    "datetimestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "content_type": file_content_type,
                    **metadata,
                }
            )

        def delete_file(self, key: str) -> None:
            """
            Delete a file from an S3 bucket
            
            params:
            :param key: key to delete the file from the bucket
            """

            self.s3.delete_object(Bucket=self.envs.s3_bucket_name, Key=key)

        def delete_files(self, prefix: str) -> None:
            """
            Delete files from an S3 bucket
            
            params:
            :param prefix: prefix to delete the files from the bucket
            """

            response = self.s3.list_objects_v2(Bucket=self.envs.s3_bucket_name, Prefix=prefix)
            
            if "Contents" in response:
                files = response["Contents"]
                self.s3.delete_objects(
                    Bucket=self.envs.s3_bucket_name,
                    Delete={
                        "Objects": [{"Key": file["Key"]} for file in files],
                    },
                )

        def list_files(self, prefix: str) -> Optional[Dict[str, str]]:
            """
            List files in an S3 bucket
            
            params:
            :param prefix: prefix to list the files from the bucket
            
            returns:
            :return: list of file objects
            """

            response = self.s3.list_objects_v2(Bucket=self.envs.s3_bucket_name, Prefix=prefix)
            
            if "Contents" in response:
                files = response["Contents"]
                response = []
                for file in files:
                    response.append({
                        "url": self.__generate_presigned_url(file["Key"]),
                        "metadata": file["Metadata"],
                    })

                return response
            
            return None

        def get_file(self, key) -> Optional[Dict[str, str]]:
            """
            Get a file from an S3 bucket
            
            params:
            :param key: key to retrieve the file from the bucket

            returns:
            :return: file object
            """

            response = self.s3.get_object(Bucket=self.envs.s3_bucket_name, Key=key)
            
            if "Body" in response:
                file_metadata = response["Metadata"]

                return {
                    "url": self.__generate_presigned_url(key),
                    "metadata": file_metadata,
                }
            
            return None

        def __generate_presigned_url(self, key: str, expires_in_seconds: int = 3600) -> str:
            """
            Generate a presigned URL for a file in an S3 bucket
            
            params:
            :param key: key to retrieve the file from the bucket
            :param expires_in_seconds: number of seconds the URL is valid for
            
            returns:
            :return: presigned URL
            """

            url = self.s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.envs.s3_bucket_name, "Key": key},
                ExpiresIn=expires_in_seconds,
            )

            return url

            
        

    