from aws_cdk import (
    aws_rds as rds,
    RemovalPolicy,
    aws_ec2 as ec2,


)
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct, vpc: ec2.Vpc, database_name: str) -> None:
        super().__init__(scope, "EurekaRDSStack")

        self.rds = rds.DatabaseCluster(
            self, "EurekaRDS",
            engine=rds.DatabaseClusterEngine.aurora_postgres(
                version=rds.AuroraPostgresEngineVersion.VER_15_6
            ),
            instance_props={
                "instance_type": ec2.InstanceType.of(
                    ec2.InstanceClass.T3, ec2.InstanceSize.MICRO
                ),
                "vpc_subnets": {
                    "subnet_type": ec2.SubnetType.PUBLIC
                },
                "vpc": vpc,
                "security_group": ec2.SecurityGroup(
                    self, "EurekaRDSSecurityGroup",
                    vpc=vpc,
                    allow_all_outbound=True
                )
            },
            instances=1,
            default_database_name=database_name,
            removal_policy=RemovalPolicy,
            credentials=rds.Credentials.from_generated_secret("postgres"),
        )
        
        self.rds.connections.allow_default_port_from_any_ipv4()
