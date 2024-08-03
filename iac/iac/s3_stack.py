import aws_cdk
from constructs import Construct
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_ecs_patterns import ApplicationLoadBalancedFargateService


class S3Stack(Construct):
    def __init__(self, scope: Construct, id: str, stage: str) -> None:
        super().__init__(scope, id)

        self.bucket = Bucket(
            self,
            "EurekaBucket" + stage,
            bucket_name=f"eureka-bucket-{stage.lower()}",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
        )

    def grant_read_write(self, service: ApplicationLoadBalancedFargateService) -> None:
        self.bucket.grant_read_write(service.task_definition.task_role)

        