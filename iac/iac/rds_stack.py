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

        self.rds = rds.ServerlessCluster(
            self, "EurekaRDS",
            engine=rds.DatabaseClusterEngine.aurora_postgres(
                version=rds.AuroraPostgresEngineVersion.VER_15_6
            ),
            vpc=vpc,
            default_database_name=database_name,
            removal_policy=RemovalPolicy.DESTROY,
            credentials=rds.Credentials.from_generated_secret("postgres"),
            scaling=rds.ServerlessScalingOptions(
                auto_pause=cdk.Duration.minutes(5),
                min_capacity=rds.AuroraCapacityUnit.ACU_1,
                max_capacity=rds.AuroraCapacityUnit.ACU_2,
            ),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),   
        )
        
        self.rds.connections.allow_default_port_from_any_ipv4()
