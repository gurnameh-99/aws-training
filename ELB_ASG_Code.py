import boto3

# Set up the AWS client
elb_client = boto3.client('elbv2')

# Create a new load balancer
elb_response = elb_client.create_load_balancer(
    Name='my-load-balancer',
    Subnets=['subnet-123456', 'subnet-789012'],  # Replace with your subnet IDs
    SecurityGroups=['sg-123456'],  # Replace with your security group ID
    Scheme='internet-facing',
    Type='application',
)

# Create a target group for the EC2 instances
tg_response = elb_client.create_target_group(
    Name='my-target-group',
    Protocol='HTTP',
    Port=80,
    TargetType='instance',
    VpcId='vpc-123456',  # Replace with your VPC ID
)

# Register the EC2 instances with the target group
elb_client.register_targets(
    TargetGroupArn=tg_response['TargetGroups'][0]['TargetGroupArn'],
    Targets=[
        {'Id': 'i-123456', 'Port': 80},
        {'Id': 'i-789012', 'Port': 80},
    ],  # Replace with your EC2 instance IDs
)

# Create a listener for the load balancer
elb_client.create_listener(
    LoadBalancerArn=elb_response['LoadBalancers'][0]['LoadBalancerArn'],
    Protocol='HTTP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': tg_response['TargetGroups'][0]['TargetGroupArn'],
        },
    ],
)

# Set up an ASG to automatically scale up or down the number of EC2 instances based on CPU utilization metrics
asg_client = boto3.client('autoscaling')

asg_response = asg_client.create_auto_scaling_group(
    AutoScalingGroupName='my-asg',
    LaunchConfigurationName='my-launch-config',  # Replace with your launch configuration name
    MinSize=2,
    MaxSize=10,
    DesiredCapacity=2,
    DefaultCooldown=300,
    AvailabilityZones=['us-west-2a', 'us-west-2b'],  # Replace with your availability zones
    TargetGroupARNs=[tg_response['TargetGroups'][0]['TargetGroupArn']],
    HealthCheckType='EC2',
    HealthCheckGracePeriod=300,
    MetricsCollection=[
        {
            'Metric': 'GroupMinSize',
            'Granularity': '1Minute',
        },
        {
            'Metric': 'GroupMaxSize',
            'Granularity': '1Minute',
        },
        {
            'Metric': 'GroupDesiredCapacity',
            'Granularity': '1Minute',
        },
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-asg',
            'PropagateAtLaunch': True,
        },
    ],
)

# Create a scaling policy for CPU utilization
asg_client.put_scaling_policy(
    AutoScalingGroupName='my-asg',
    PolicyName='my-scaling-policy',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization',
        },
        'TargetValue': 50.0,  # Adjust as needed
    },
)
