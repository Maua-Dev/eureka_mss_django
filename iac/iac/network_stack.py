from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
)
from constructs import Construct


class NetworkStack(Construct):
    def __init__(self, scope: Construct, **kwargs) -> None:
        super().__init__(scope, "EurekaNetworkStack")

        # Our network in the cloud
        self.vpc = ec2.Vpc(
            self,
            "EurekaVPC",
            max_azs=2,  # default is all AZs in region
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )
        self.ecs_cluster = ecs.Cluster(self, f"EurekaECSCluster", vpc=self.vpc)
        # Add VPC endpoints to keep the traffic inside AWS


