## AMIs (Amazon Machine Images)

An AMI is a blueprint for setting up an EC2 instance, with dependencies and applications installed.

![Setting up an AMI on AWS](../diagrams/AMI_set_up.png)

### Building AMI

- Ensure the instance you want to create a blueprint for is running or stopped.
- Under Actions, Images and Templates select `Create Image`.
- Use the naming conventions in the above diagram.

### Launching an EC2 instance from your AMI

- On the AMIs tab of AWS, select the AMI and `Launch instance with AMI`.
- Configure as above for EC2 instance, and launch.
- Any applications and dependencies will be automatically configured, but any connections between instances using IPs will have to be set manually, as AWS reassigns new public IPs for each instance.
- Note: to `ssh` in the instance, you may need to change `root` to `ubuntu` when you copy the ssh command from 'Connect' page for the instance.

### Advantages of AMIs
- Can launch multiple instances with the same configuration and set up, adapting and scaling to meet business requirements.
- Can reuse blueprints years later without memorising the set up details.
- Decreases deployment time due to the reduced manual installations.
- Can safely terminate instances without losing the set-up, reducing running costs.
- Can choose from a variety of operating systems.