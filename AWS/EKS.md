## AWS EKS (Amazon Managed Elastic Kubernetes Service)

- Its a way to launch managed Kubernetes cluster on AWS
- Kubernetes is an opensource system for automatic deployment, scaling and management of containerized (usually Docker) application
- It's an alternative to ECS, similar goal but different API
- EKS supports EC2 if wanted to deploy worker nodes or Fargate to deploy serverless containers
- Use cases: If your company is already using K8s on-prem or in another cloud, and wants to migrate to AWS using K8s
- Kubernetes is cloud-agnostic (can be used in any clous - Azure, GCP...)

* Node Types:
    - Managed Nodes Groups: 
        - Creates and manages Nodes (EC2) for us
        - Nodes are part of an ASG managed by EKS
        - Supports on-demand or spot instances
    - Self-Managed Node Groups
        - Nodes created by us and registered to the EKS cluster and managed by an ASG
        - Can use pre-build AMI - Amazon EKS Optimized AMI
        - Supports on-demand or spot instances
    - Fargate
        -No maintenance required, no nodes managed

* Data Volumes:
    - Need to specify StorageClass manifest on your EKS cluster
    - Leverage a Container Storge Interfact (CSI) compliant driver
    - Supports: EBS, EFS (only fargate), FSx for Lustre, FSx for NetApp ONTAP