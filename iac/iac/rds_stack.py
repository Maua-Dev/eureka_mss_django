from aws_cdk import (
    aws_rds as rds,
    RemovalPolicy,
    aws_ec2 as ec2,
)
import aws_cdk as cdk
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct, vpc: ec2.Vpc, database_name: str) -> None:
        super().__init__(scope, "EurekaRDSStack")

        self.rds = rds.DatabaseCluster(
            self,
            "EurekaRDS",
            engine=rds.DatabaseClusterEngine.aurora_postgres(
                version=rds.AuroraPostgresEngineVersion.VER_15_6
            ),
            default_database_name=database_name,
            removal_policy=RemovalPolicy.DESTROY,
            vpc=vpc,
            serverless_v2_max_capacity=1,
            serverless_v2_min_capacity=0.5,
            credentials=rds.Credentials.from_generated_secret("postgres"),
        )
        
        self.rds.connections.allow_default_port_from_any_ipv4()
