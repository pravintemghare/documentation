# Terraform Provisioners

- Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction.

## Types of provisioners

### Local-exec
- local-exec provisioners allow us to invoke local executable after resource is created
- One of the most used approach for local-exec is to run ansible-playbooks on the created server after the resource is created.

### Remote-exec
- remote-exec provisioner allow us to invoke scripts directly on the remote server.

## Primary provisioners

### Creation Time Provisioners
- Are only run during creation, not during updating or any other lifecycle. If this fails the resource is marked as tainted.

### Destory Time Provisioners
- Are run before the resources are destroyed.


- If "when = destory" is specified the provisioner will run when the resource is destroyed.


## Provisioner - Failure Behaviour

- By default, provisioners that fail will also cause the terraform apply itslef to fail. 
- The ```on_failure``` setting can be used to change this. The allowed values:
    - continue = Ignore the error and continue with creation or destruction
    - fail = Raise an error and stop applying/destroying If this is a creation provisioner taint the resource.