import datetime
import boto3
from botocore.config import Config
from app.environments import Environments


class HelperGenerateUrl:
    S3_BUCKET_NAME = Environments.get_envs().s3_bucket_name

    def get_presigned_url(self, project_id: int, upload_type: str, file_name: str) -> dict:

        my_config = Config(
            region_name=Environments.get_envs().region,
            signature_version="s3v4"
        )

        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=Environments.get_envs().aws_access_key_id,
            aws_secret_access_key=Environments.get_envs().aws_secret_access_id,
            config=my_config,
        )

        time_created = int(datetime.datetime.now().timestamp() * 1000)

        key = self.generate_key(project_id=project_id,
                                upload_type=upload_type,
                                file_name=file_name,
                                time_created=time_created)

        meta = {
            "project_id": "project_id",
            "upload_type": upload_type,
            "time_created": str(time_created)
        }

        try:
            presigned_url = self.s3_client.generate_presigned_url(
                ClientMethod='put_object',
                Params={
                    'Bucket': self.S3_BUCKET_NAME,
                    'Key': key,
                    'Metadata': meta
                },
                ExpiresIn=600,
            )

        except Exception as e:
            print("Error while trying to upload file to S3")
            print(e)
            raise e

        cloud_front_distribution_domain_assets = Environments.get_envs().cloud_front_distribution_domain_assets
        if cloud_front_distribution_domain_assets is None:
            cloud_front_distribution_domain_assets = ""  


        presigned_url = presigned_url.replace(
            f"{self.S3_BUCKET_NAME}.s3.amazonaws.com", cloud_front_distribution_domain_assets)

        return {
            "url": presigned_url,
        }

    def generate_key(self, project_id: int,
                     upload_type: str,
                     file_name: str,
                     time_created: int) -> str:

        return f"{project_id}/{upload_type}/{file_name}/{time_created}"
