The code in this repository is a collection of scripts and files I used to learn aws.
In order to run this you must set up your own aws account first.
The mini projects are done using boto3 the aws python SDK.

Following are the description of files
- ELB_ASG_Code.py : This code creates a new load balancer with a target group for the EC2 instances, and then sets up an ASG to automatically scale the number of instances based on CPU utilization metrics.

- EC2_Storage.py : This code launches a new EC2 instance and configures it to use instance storage for temporary data storage. It also attaches an EBS volume for persistent data storage, and prints information about the instance and volume. You can experiment with different instance types by changing the InstanceType parameter, and you can attach additional EBS volumes by calling the create_volume and attach_volume methods again with different parameters. Note that you may need to adjust the device name (/dev/sdf in this example) depending on the number of block devices already attached to the instance.

- Route53.py - This script creates a new hosted zone for the domain name 'example.com', creates A records for an EC2 instance and a load balancer, and configures weighted routing, latency-based routing, and geolocation routing policies. It also creates health checks for the resources to monitor their availability and associate them with the resource record sets. You'll need to replace the values for the IP address, DNS name, hosted zone ID, and other parameters with your own values.

- three-tier-app - ![Architecture Diagram](https://github.com/aws-samples/aws-three-tier-web-architecture-workshop/blob/main/application-code/web-tier/src/assets/3TierArch.png)
    In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal facing load balancer then forwards that traffic to the application tier, which is written in Node.js. The application tier manipulates data in an Aurora MySQL multi-AZ database and returns it to our web tier. Load balancing, health checks and autoscaling groups are created at each layer to maintain the availability of this architecture.

- ECS-Cluster - launch containerized applications on a new ECS cluster using Fargate, use ECR to store and manage container images and EKS to deploy and manage Kubernetes clusters. Experiment with different container orchestration techniques, including load balancing, scaling, and service discovery using AWS CLI.

- database - sample codes to functionalities of rds and neptune

- data-analytics - The provided Python code demonstrates the use of the Kinesis Client Library (KCL) to process data from a Kinesis stream, and store it in DynamoDB. It defines the KCL configuration and runs the KCL process using the KCLProcess class.

- ml - The provided Python codes demonstrate how to use AWS Rekognition for image analysis, Transcribe for audio transcription, and Textract for text and data extraction from documents. Proper AWS authentication is required.



