# AWS Auto Scaling groups (AWS ASGs)

- AWS autoscaling manages the number of instances available to handle the load for your application.
- An ASG contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.
- You specify the min, max and desired number of instances.
- Starts by launching enough instances to meet desired capacity.
- With specified scaling policies, the Auto Scaling launches and terminates instances as demand on an application increases or decreases.

## Elastic load balancing
- Automatically distributes incoming traffic across instances so that no instance is overwhelmed.
- Can attach diferent types for different requirements.

## Launch templates
- Specifies configuration information, such as instance type, AMI, key pair, security groups.
- Unlike a launch configuration, you create multiple versions of a template - for e.g., you can define a base configuration without an AMI, and then luanch a new version with an AMI and user data that has the latest version of an application for testing.
- Note as well that now all AWS Auto Scaling features are available for luanch configurations.

## Autoscaling policy options
- Target-tracking: select scaling metric and set target values, and then AWS adds or removes capacity to adjust the metric to be as close to the target value.
- Metrics include average CPU utilisation, average number of bytes recieved/sent out on network interfaces, or the average load balancer request count.
- Simple and step scaling policies use metrics and threshold values that are used to trigger the scaling policy.
- The difference with step scaling is that the adjustments vary based  on the size of the alarm breach.