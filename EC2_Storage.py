import boto3

# Set up the AWS client
ec2_client = boto3.client('ec2')

# Launch a new EC2 instance with instance storage
instance_response = ec2_client.run_instances(
    ImageId='ami-123456',  # Replace with your desired AMI ID
    InstanceType='m5.large',  # Replace with your desired instance type
    KeyName='my-key-pair',  # Replace with your desired key pair name
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'VirtualName': 'ephemeral0',
        },
    ],
)

# Wait for the instance to be running
instance_id = instance_response['Instances'][0]['InstanceId']
ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Retrieve the instance's metadata
instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]

# Attach an EBS volume for persistent data storage
volume_response = ec2_client.create_volume(
    AvailabilityZone=instance['Placement']['AvailabilityZone'],
    Size=50,  # Replace with your desired volume size
)

ec2_client.get_waiter('volume_available').wait(VolumeIds=[volume_response['VolumeId']])

ec2_client.attach_volume(
    Device='/dev/sdf',
    InstanceId=instance_id,
    VolumeId=volume_response['VolumeId'],
)

# Print the instance and volume information
print(f"Instance ID: {instance_id}")
print(f"Instance type: {instance['InstanceType']}")
print(f"Instance storage: {instance['BlockDeviceMappings']}")
print(f"EBS volume ID: {volume_response['VolumeId']}")
