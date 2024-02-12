## Terrform
- Free and opensource tool. Developed by HashiCorp
- Ability to deploy infrastructure on multiple providers
    - Physical Machine
    - VMware
    - AWS
    - Azure
    - GCloud

- Terraform uses Hashi Corp Language - Simple declarative language which has blocks of code for infrastructure deployment
- Files with .tf extension are used in terraform
- Works in 3 phases:
    - init phase where terraform initialize the project and identify the providers for the target env
    - plan phase terraform drafts a plan for the target stage
    - apply phase terraform make the necessary changes on the target env 

- Terraform manages resources 
- Records the stage of the resoruces and decided what action to be taken to make it desired stage
- Can import resources created outside of terraform and bring under its control

- It is recommened to create all resources in on file and name it as main.tf. Other files which can be created are:
    - main.tf - main config file containing resources
    - variable.tf - contains variables declarations
    - output.tf - contains outputs from resources
    - providers.tg - contains providers information

## Resource Attributes
- Reference one resource with other resources
- `${resource_provider.resource_name.attribute}`

## Resoruce Dependencies
- The dependent resources are created first and while deleting the dependent resources are deleted later
depends_on = [
    random_pet.mypet
]

## Output variables
- We can have output of our resources created in terraform
ouput pet_name {
    value = random_pet.my-pet.id
    description = "A valid discription"
}

- The output variables are printed on the screen
- `terraform output` can print the output variables
- This can be used in to feed data to other IAC tools

## Command
- `terraform validate` - to check syntax of the configuration
- `terraform show` - show current state of the infrastructure
- `terraform refresh` - to refresh the state file and modify accordingly
- `terraform graph` - this can be pass through various graph utility (graphviz)

## Mutable & Immutable infrastructure
- The infrastructure which can be changed is called mutable
- Immutable infrastructe are recreated with a new version of deployment

## Lifecycle rules
- `create_before_destory` This will create new resource before deleting
- `prevent_destory` This will only prevent changes only in apply not in destroy command
- `ignore_changes` This will ignore a particular argument change

resource local_file test {
    filename = "test.txt"
    lifecycle {
        create_before_destory = true
        prevent_destory = true
        ignore_changes = [
            tags
        ]
    }
}

## Datasource
- We can import resources in terraform as a data source which are already create

data "local_file" "text" {
    filename = "text.txt"
}

## Meta-Arguments
- Meta-Arguments are depends_on & lifcycle
- `count`

resources "local_file" "test" {
    filename = "test.txt"
    count = 3
}

variable "filename" {
    type = list
    default = [
        test.txt
        test1.txt
    ]
}
resources "local_file" "text" {
    filename = var.filename.[count.index]
    count = 3
    count = length(var.filename)
}

## For loop
- `for_each`
- only works with maps or set
- resources are stored as map

variable "filename" {
    type = set(string)
    default = [
        test.txt
        test1.txt
    ]
}
resources "local_file" "text" {
    filename = each.value
    for_each = var.filename
    for_each = toset(var.filename)
}

## Version Constraints
- We can use a specific version of providers in terraform
- It can be used in terraform block

terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
            version = "1.4.0"
            version = "!= 2.0.0." - downloads the previous version
            version = "< 1.5.6"
            version = "> 1.2.1"
            version = "> 1.2.3, < 2.0.0, != 2.2.2"
            version = "~< 1.2" starting from 1.2
            version = "~> 1.2.0" 
        }
    }
}