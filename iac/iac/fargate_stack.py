from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_rds as rds,
    aws_elasticloadbalancingv2 as elbv2,
)
from constructs import Construct


class FargateStack(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.Vpc,
        ecs_cluster: ecs.Cluster,
        rds_instance: rds.DatabaseInstance,
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
            cpu=self.task_cpu,  # Default is 256
            memory_limit_mib=self.task_memory_mib,  # Default is 512
            desired_count=self.task_desired_count,  # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset(
                    directory="../",
                    file="Dockerfile",
                ),
                container_name=self.container_name,
                container_port=8000,
                environment={
                    "STAGE": stage,
                    "DJANGO_SETTINGS_MODULE": "eureka_api.settings",
                    "DB_NAME": database_name,
                    "DB_USER": rds_instance.secret.secret_value_from_json("username").unsafe_unwrap(),
                    "DB_PASSWORD": rds_instance.secret.secret_value_from_json("password").unsafe_unwrap(),
                    "DB_HOST": rds_instance.db_instance_endpoint_address,
                    "DB_PORT": rds_instance.db_instance_endpoint_port,
                },
            ),
            public_load_balancer=True,
            assign_public_ip=True,
        )

        # Configure the target group health check
        self.alb_fargate_service.target_group.configure_health_check(
            path="/status/",
            healthy_threshold_count=3,
            unhealthy_threshold_count=2,
        )

        # Capturing the Fargate dns name
        alb_dns = self.alb_fargate_service.load_balancer.load_balancer_dns_name

        # Adding the Fargate host to the environment
        self.alb_fargate_service.task_definition.default_container.add_environment(
            "DJANGO_ALLOWED_HOSTS", alb_dns
        )
