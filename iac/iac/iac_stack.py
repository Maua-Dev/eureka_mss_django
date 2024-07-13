import os

from aws_cdk import (
    Stack,
    aws_ec2 as ec2, aws_ecs as ecs, aws_ecs_patterns as ecs_patterns,
    aws_ecr as ecr
)

from constructs import Construct

class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ENVIRONMENT = {
            "STAGE": os.environ.get("STAGE", "test"),
            "REPOSITORY_NAME": os.environ.get("REPOSITORY_NAME")
        }

        vpc = ec2.Vpc(self, "EurekaApiVPC", max_azs=2)

        cluster = ecs.Cluster(self, "EurekaApiCluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "EurekaApiService",
            cluster=cluster,
            memory_limit_mib=1024,
            cpu=512,
            task_image_options={
                "image": ecs.ContainerImage.from_registry(f"{ENVIRONMENT['REPOSITORY_NAME']}:latest"),
                "container_port": 8000,
            },
            public_load_balancer=True,
        )
