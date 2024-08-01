import os

from aws_cdk import (
    CfnOutput,
    aws_rds as rds,
    RemovalPolicy,
    aws_ec2 as ec2,


)
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct, vpc: ec2.Vpc) -> None:
        super().__init__(scope, "EurekaRDSStack")

        self.rds = rds.DatabaseInstance(
            self,
            "EurekaRDS",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15_4
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T3, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            credentials=rds.Credentials.from_generated_secret("postgres"),
            removal_policy=RemovalPolicy.DESTROY,
            database_name="eureka_db",
            publicly_accessible=True,
            storage_type=rds.StorageType.GP3,
            allocated_storage=20,
            max_allocated_storage=100,
        )

        self.rds.connections.allow_default_port_from_any_ipv4()



