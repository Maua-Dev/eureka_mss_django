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
        self.project_name = os.environ.get("PROJECT_NAME")
        self.respository_name = os.environ.get("REPOSITORY_NAME")

        REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.STAGE else RemovalPolicy.DESTROY

        self.network_stack = NetworkStack(self, "EurekaNetworkStack")

        self.rds_stack = RDSStack(self, self.network_stack.vpc)

        self.fargate_stack = FargateStack(
            self,
            "EurekaFargateStack",
            rds_instance=self.rds_stack.rds, 
            vpc=self.network_stack.vpc,
            ecs_cluster=self.network_stack.ecs_cluster, 
            repository_name=self.respository_name
        )
