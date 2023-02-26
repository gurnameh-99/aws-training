The code in this repository is a collection of scripts and files I used to learn aws.
In order to run this you must set up your own aws account first.
The mini projects are done using boto3 the aws python SDK.

Following are the description of files
- ELB_ASG_Code.py : This code creates a new load balancer with a target group for the EC2 instances, and then sets up an ASG to automatically scale the number of instances based on CPU utilization metrics.

- EC2_Storage.py : This code launches a new EC2 instance and configures it to use instance storage for temporary data storage. It also attaches an EBS volume for persistent data storage, and prints information about the instance and volume. You can experiment with different instance types by changing the InstanceType parameter, and you can attach additional EBS volumes by calling the create_volume and attach_volume methods again with different parameters. Note that you may need to adjust the device name (/dev/sdf in this example) depending on the number of block devices already attached to the instance.
