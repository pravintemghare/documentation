# Remote State Management

## Git Ignore
- The .gitignore file is a text file that tells Git which files or folders to ignore in a project.
- Files to ingore in terraform:
    * .terraform
    * terraform.tfvars
    * terraform.tfstate
    * carsh.log

## Terraform Backend
- Backend primarily determine where Terraform stores its state.
- By default, Terraform implicitly uses backend called local to store state as a local file on disk.
- Terraform project is handled and collaborated by an entire team.
- Storing the state file in the local laptop will not allow collaboration.
- Terraform supports multiple backend that allows remote service releated operations:
    S3, Consul, Azurerm, Kubernetes, HTTP, ETCD

## Ideal Architecture 
- Following describes one of the recommended architecture:
    - The terraform code is stored in git repository
    - The state file is stored in a central backend

- Accessing state in a remote service generally requires some kind of access credentails.
- Some backends act like plain 'remote disks' for state files, others support locking the state while operations are being performned which helps prevents conflicts and inconsistencies.

## State Lock
- Whenver performing write operation terraform would lock the state file. This is very important as otherwise during your ongoing terraform apply operations, if others also try for the same it could corrupt your state file.
- State locking happens automatically on all operations that could write state. You won't see any message that it is happening.
- If state locking fails Terraform will not continue.
- Not all backends support locking. The documentation for each backend includes details on whether it supports locking or not.

### Force unlocking
- Terraform has a 'force-unlock' command to manually unlock the state if unlocking failed.
- If you unlock the state when someone else is holding the lock it could cause multiple writes.
- Force unlock should only be used to unlock your own lock in the situation where automatic unlocking failed.

## Sate Locking in S3
- By default S3 doesn't support State Locking functionality
- You need to make use of Dynamo DB table to achieve state locking functionality 

## State Modification
- As your terraform usage becomes more advanced there are some cases where you may need to modify the Terraform state.
- It is important to never modify the state directly. Instead make use of terraform state command.

```terraform state``` - command to modify state.
- Sub commands:
    * list = to view resources created
    * mv = move items with terraform state
    * pull = manually download and output the state from remote state.
    * push = manually upload local state file to remote.
    * rm = to remove items from terraform state.
    * show = to show the attributes of a single resource in the state.

### Terraform remote state
- The ```terraform_remote_state``` data source retrives the root module output values from some other Terraform configuration using the latest state snapshot from the remote backend.


## Terraform Import
- It can happen that all the resources in an organization are created manually. Organization now wants to start using terraform and manage these resources. 
- In older approach Terraform import would create the state file assoicated with the resources running in your environment. Users still had to write the tf files from scratch. 
- In newer approach terraform import can automatically create the terraform configuration files from the resources you want to import.
- Terraform version 1.5 introduces automatic code generation for imported resources. 
- This can drastically reduce the amount of time you spend writing code to match the imported. 
- This feature is not available in older version of terraform.

import {
    to = aws_security_group.mysg
    id = sg-eqwdqcwqe121212
}