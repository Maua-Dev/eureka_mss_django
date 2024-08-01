import os
from aws_cdk import (
    Stack,
    RemovalPolicy
)
from constructs import Construct


from .rds_stack import RDSStack
from .fargate_stack import FargateStack
from .network_stack import NetworkStack


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.STAGE = os.environ.get("STAGE")

        DB_NAME = "eureka_db"

        self.network_stack = NetworkStack(self, "EurekaNetworkStack")

        self.rds_stack = RDSStack(self, self.network_stack.vpc, DB_NAME)

        self.fargate_stack = FargateStack(
            self,
            "EurekaFargateStack",
            rds_instance=self.rds_stack.rds, 
            vpc=self.network_stack.vpc,
            ecs_cluster=self.network_stack.ecs_cluster,
            database_name=DB_NAME,
            stage=self.STAGE
        )
