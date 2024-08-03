import os
from aws_cdk import (
    Stack,
)
from constructs import Construct


from .s3_stack import S3Stack
from .rds_stack import RDSStack
from .fargate_stack import FargateStack
from .network_stack import NetworkStack


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.STAGE = os.environ.get("STAGE").upper()

        DB_NAME = "eureka_db"

        self.network_stack = NetworkStack(scope=self)

        self.rds_stack = RDSStack(self, self.network_stack.vpc, DB_NAME)

        self.s3_stack = S3Stack(self, "EurekaS3Stack", self.STAGE)
        
        self.fargate_stack = FargateStack(
            self,
            "EurekaFargateStack",
            rds_instance=self.rds_stack.rds, 
            vpc=self.network_stack.vpc,
            ecs_cluster=self.network_stack.ecs_cluster,
            s3=self.s3_stack.bucket,
            database_name=DB_NAME,
            stage=self.STAGE
        )

        # Grant read/write permissions to the Fargate service
        self.s3_stack.grant_read_write(self.fargate_stack.alb_fargate_service)
