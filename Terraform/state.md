## Terraform State
- Workflow - init, plan & apply
- In plan stage terraform refersh the state and tells us if anything will be deleted/create/modified
- Terraform has a unique id for each resource created
- In the working directory a file call terraform.tfstate - It is not created until the apply command is run at once


## Purpose of state in terraform
- It helps to identify the difts happened in the real world vs the working directory
- terraform plan --refresh=false to not to refresh state it takes from the cache
- Collabration when working as a team
- We can store state files in S3, GCP storage, HashiCorp Consul, HashiCorp Cloud

## State Considerations
- We should consider storing the state file always in a secured storage

