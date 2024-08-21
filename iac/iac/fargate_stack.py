from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_rds as rds,
    aws_elasticloadbalancingv2 as elbv2,
    aws_s3 as s3,
)
from constructs import Construct


class FargateStack(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.Vpc,
        ecs_cluster: ecs.Cluster,
        s3: s3.Bucket,
        rds_cluster: rds.ServerlessCluster,
        task_cpu: int = 256,
        task_memory_mib: int = 1024,
        task_desired_count: int = 1,
        task_min_scaling_capacity: int = 2,
        task_max_scaling_capacity: int = 4,
        database_name: str = None,
        stage: str = None,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id)
        self.vpc = vpc
        self.ecs_cluster = ecs_cluster
        self.task_cpu = task_cpu
        self.task_memory_mib = task_memory_mib
        self.task_desired_count = task_desired_count
        self.task_min_scaling_capacity = task_min_scaling_capacity
        self.task_max_scaling_capacity = task_max_scaling_capacity

        self.container_name = f"eureka_django_app"

        # Create the load balancer, ECS service and fargate task for teh Django App
        self.alb_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            f"EurekaDjangoAppService",
            protocol=elbv2.ApplicationProtocol.HTTP,
            platform_version=ecs.FargatePlatformVersion.VERSION1_4,
            cluster=self.ecs_cluster,  # Required
            cpu=self.task_cpu,
            memory_limit_mib=self.task_memory_mib,
            desired_count=self.task_desired_count,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset(
                    directory="../",
                    file="Dockerfile",
                ),
                container_name=self.container_name,
                container_port=8000,
                environment={
                    "STAGE": str(stage),
                    "DJANGO_SETTINGS_MODULE": "eureka_api.settings",
                    "DB_NAME": str(database_name),
                    "DB_USER": str(rds_cluster.secret.secret_value_from_json("username").unsafe_unwrap()),
                    "DB_PASSWORD": str(rds_cluster.secret.secret_value_from_json("password").unsafe_unwrap()),
                    "DB_HOST": str(rds_cluster.cluster_endpoint.hostname),
                    "DB_PORT": str(rds_cluster.cluster_endpoint.port),
                    "S3_BUCKET_NAME": str(s3.bucket_name),
                },
            ),
            public_load_balancer=True,
        )

        # Configure the target group health check
        self.alb_fargate_service.target_group.configure_health_check(
            path="/status/",
            healthy_threshold_count=3,
            unhealthy_threshold_count=2,
        )
