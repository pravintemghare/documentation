# Terraform Cloud

## Overview
- Terraform cloud manages terraform runs in a consistent and reliable environment with various features like access control, private registry for sharing modules, policy controls and other.


## Sentinel
- Sentinel is a policy-as-code framework intergrated with the HashiCorp Enterprise products
- It enables fine-grained, logic-based policy decisions, and can be extended to use information from external sources.
- It is a paid feature

## Remote Backend
- Terraform backend stores Terraform state and may be used to run operations in Terraform Cloud. 
- Terraform Cloud can be used with local operations, in which case only state is stored in the Terraform Cloud backend.

## Remote Operations
- When using full remote operations, operations like terraform plan or apply can be executed in Terraform Cloud's run environment, with log output streaming to the local terminal.


## Air Gap System
- An air gap system is a network security measure employed to ensure that a secure computer network is physically isolated from unsecured networks, such as public subnets.
- Air gapped environments are used in various areas. Some of these includes:
    - Military/ Governmental computer network/systems
    - Financial computer systems, such as stock exchanges
    - Industrial control systems, such as SCADA in Oil and Gas Fields
- Terraform enterprise installs using either an online or air gapped method and as the name infer, one requires internet connectivity, the other doesn't 