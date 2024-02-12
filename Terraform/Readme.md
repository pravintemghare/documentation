
## Terraform commands 

## Main Command 
```
```terraform init``` -- To initialize the directory in which working and download all the required providers plugins. Downloaded to .terraform directory.
```terraform validate``` -- To validate our terraform files and check for report for any error.
```terraform plan``` -- Create an execution plan for terraform apply. 
```terraform plan -out myplan``` -- To save the plan in an output
```terraform apply``` -- To create infrastructure according to the plan created.
```terraform apply myplan``` -- To create infrastructure according to the plan stored.
```terraform destroy``` -- To delete resources created by terraform apply.
```terraform destroy -target aws_instance.myec2``` -- To delete a specific resource in terraform. Target is a combination of resource type and local resource name.
```terraform refresh``` -- To check tha latest state of your infrastructure and update the state file accordingly. 
```terraform fmt``` -- To rewrite the terraform configuration file to take care of the overall formating.
```terraform output local_resource_name```  --- To get output using command.
```

- To comment multiple lines in terraform /* code */



## Providers
- A provider is a plugin that lest Terraform manange an external API.
- There are primary 3 types of providers
    - Official = Maintained by HarisCorp
    - Partner = Owned and maintained by technology company that maintains direct partnership with HarisCorp
    - Community = Owned and maintained by individual contributors.

### Providers Versioning
- Providers plugins are released separately from Terraform itself.
- During terraform init command if the version argument is not provided, the most recent provider will be downloaded during initialization.

### Arguments for version selection
>= 1.0 = Greater than equal to
<= 4.0 = Less than equal to
~> 2.0 = Any version of 2.x range
>= 2.0,<=3.0 = Any version between 2 & 3
 
### Official provider:
provider "aws" {
    region = "us-east-1"
    version = "~= 1.0.0"
    access_key = "ACCESS_KEY"
    secret_key = "SECRET_KEY"
}

### Partner provider:
terraform {
    required_providers {
        digitalocean = {
            source = "digitalocean/digitalocean"
        }
    }
}

provider "digitalocean" {
    token = "TOKEN_HERE"
}
## Resources
- A resource block describes one or more infrastructure objects.

### Dependency Lock
- Terraform dependency lock file allows us to lock to a specific version of the provider.
- If a particular provider already has a selection recorded in the lock file, Terraform will always re-select that version for installation, even if a newer version has become available.
- You can overide that behaviour by adding the upgrade option when you run terraform init.






## Terraform Settings

### Setting1 - Version
- The required_version setting accepts a version constraint string, which specifies which version of Terraform can be used with your configuration
- If the running version of Terraform doesn't match the contraints specified, Terraform will procduce an error and exit without taking any further actions.

terraform {
    required_version = "0.13"
    required_providers {
        aws = "> 2.0"
    }
}






## Terraform state file

- Terraform stores the state of the infrastructure that is being created from the TF files.
- This state allows terraform to map real world resource to your exiting configuration.
- The state is stored in the file "terraform.tfstate".
- If state files doesn't exists there is no track of infrastructure created earlier. So it would recreate the infrastructure again.

### Desired State:
    Terraform primary function is to create, modify and destroy infrastructure resources to match the desired state described in a Terraform configuration.

### Current State:
    Is the actual state of a resource that is currently deployed.

- Terraform tries to ensure that the deployed infrastructure is based on the desired state. If there is a difference between the two, terraform plan presents a description of the changes necessary to achieve the desired state.

### Terraform Refresh
    You should not tipically need to use this command because Terraform automatically performs the same refreshing actions as a part of creating a plan in both the terraform plan and terraform apply commands.

    This command is depricated in the newer version of terraform. The refresh-only option for terraform plan and terraform apply was introduced in terraform v0.15.4





## Terraform Cross Resource Attribute References
- It can happen that in a single terraform file, you are defining two different resources. However resouce 2 might be dependent on some value of resource 1.
- Each resource has its associated set of attributes. Attributes are the fields in a resource that hold the values that end up in state.
- Terraform allows us to reference the attribute of one resource to be used in a different resource.
- Reference ```[resource_name.local_resource_name.attribute_name]```
- To use it with other values ```["${resource_name.local_resource_name.attribute_name}/text"]```






## Output in terraform

- Output make information about your infrastrcture available on the command line and can expose information for another Terraform configurations to use
- Output values defined in Project A can be reffered from code in Project B as well.

output "output_name" {
    value = resource_name.local_resource_name.attribute_name
}

```terraform output local_resource_name```  --- To get output using command.






## Local Values

- A local value assigns a name to an expression, allowing it to be used multiple times within a module without repeating it.
- Local values can be helpful to avoid repeating the same values or expressions multiple times in a configuration.
- If overused they can also make a configuration hard to read by future maintainers by hiding the actual values used.
- Use local values only in moderation, in situations where a single value or result is used in many places and that value is likely to be changed in future.

locals {
    common_tags = {
        Owner = "DevOps team"
        service = "backend"
    }
}

resource "aws_instance" "prod" {
    ami = "ami-adadcq2f3qveqe"
    instance_type = "m5.large"
    tags = locals.common_tags
}






## Terraform Functions
- The terraform language includes a number of built-in functions that you can use to transfer and combine values.
- The general syntax for functions calls is a function name followed by comma-seperated arguments in parentheses:
  ```function (argument1, argument2)```
  ```max (5, 12, 9)```  -- output 12
- User defined functions are not supported in terraform language, only the functions built in to the language are available to use.
    - Numeric
    - String
    - Collection
    - Encoding
    - Filesystem
    - Date and Time
    - Hash & Crypto
    - IP Network
    - Type Conversion






## Data Source
- Data Source allow data to be feteched or computed for use elsewhere in Terraform Configuration.
- Defined under data block
- Reads from a specific data source(aws_ami) and exports results under  "app_ami"

EG:
data "aws_ami" "app_ami {
    most_recetn = true
    owner = ["amazon]

    filter {
        name = "name"
        values = ["amzn2-ami-hvm"]
    }
}

resource "aws_instance" "web1" {
    ami = data.aws_ami.app_ami
    instance_type = t2.mmicro
}






## Debugging in Terraform

- Terrform has detailed logs which can be enabled by setting the TF_LOG environment variable to any value.
- You can set TF_LOG to one of the log levels TRACE, DEBUG, INFO, WARN or ERROR to change the verbosity of the logs
- TRACE is the most verbose and it is the default if TF_LOG is set to something other than a log level name
- To persist logged output you can set TF_LOG_PATH in order to force the log to always be appended to a specific file when logging is enabled.
```export TF_LOG=TRACE```
```export TG_LOG_PATH=/var/log/terraformlog```





## Dynamic Blocks

- Allows to dynamically construct repeatable nested blocks which is supported inside resource, data, provider, and provisioner blocks.

variable sg_ports {
    type = list(number)
    default = [80,443,8080,22]
}

resource "aws_security_group" "dynamic_sg" {
    name = "dynamic_sg"

    dynamic "ingress" {
        for_each = var.sg_ports
        content {
            from_port = ingress.value
            to_port   = ingress.value
            protocol  = "tcp"
            cidr_blocks = [0.0.0.0/0]
        }
    }
}

### Iterators

- The iterators arguments(optional) sets the name of a temporary variable that represents the current element of the complex value.
- If ommited the name of the variable defaults to the label of the dynamic block (ingress in the example below)

variable sg_ports {
    type = list(number)
    default = [80,443,8080,22]
}

resource "aws_security_group" "dynamic_sg" {
    name = "dynamic_sg"

    dynamic "ingress" {
        for_each = var.sg_ports
        iterator = port
        content {
            from_port = port.value
            to_port   = port.value
            protocol  = "tcp"
            cidr_blocks = [0.0.0.0/0]
        }
    }
}






## Tainting Resources

- Dealing with manual changes
- Two ways to deal with this: Import Changes to Terraform / Delets & Recreate the resource

### Recreating the resource
- The -replace option with terraform apply to force Terraform to replace an object even though there are not configuration changes that would require it.

```terraform apply -replace="aws_instance.web1"```

- Similar kind of functionality was achived using ```terraform taint``` command in older version of Terraform






## Splat Expression 

- Allows to get a list of all the attributes

resource "aws_iam_users" "users" {
    name = "iamuser.${count.index}"
    count = 3
    path = "/system/"
}

output "arn" {
    value = aws_iam_users.users[*].arn  --- To get out put of all users
    value = aws_iam_users.users[1].arn  --- To get out put of 2nd user in the list
}






## Terraform graph

- The terraform graph command is used to generate a visual representation of either a configuration or execution plan.
- The output of terraform graph command is in the DOT format, which can easily be converted to an image.
- Graph viz can be used to convert .dot to image file 






## Dealing with large infrastructure

- Switch to smaller configuration were each can be applied independently.
- We can prevent from quering the current state during operations like terraform plan. This can be achieved with the 
  ```-refresh=false``` flag 
- The "-target=resource" flag can be used to target a specific resource.
- Generally used as a means to operate on isolated portions of very large infrastrucutre.
```terraform plan target=ec2```






## Zipmap function

- The zipmap function constructs a map from a list of key and a corresponding list of values.

--- zipmap ([1,2,3],[one,two,three])
{
    "1" = "one"
    "2" = "two"
    "3" = "three"
}

- Useful while creating output






## Comments in terraform

- A comment is a text note added to the source code to provide explanatory information, usually about the function of the code.
- Terraform language supports 3 different types of comments

-- #        ---- single line comment
-- //       ---- single line comment alternative to #
-- /* & */  ---- multiple line comment






## Resource Behaviour & Meta Arguments

- Create resources that exist in the configuration but are not associated with a real infrastructure object in the state. 
- Destroy resources that exist in the state but no longer exist in the configuration.
- Update in-place resources whose arguments have changed.
- Destroy and re-create resources whose arguments are changed but which cannot be updated in-place due to remote API limitation.


- Terraform allows us to include meta-argument with the resource block which allows some details of the standard resource behaviour to be customized on a pre-resource basis.

### Meta Arguments

depends_on --- handles hidden resource or module dependency that Terraform cannot automatically infer.
count --- Accepts a whole number, creates that many instances of the resource.
for_each --- accepts a map or set of strings, and creates an instance of each item in that map or set.
lifecycle --- allows modification of the resoruce lifecycle.
provider --- specifies which provider to use for a resource, overriding Terraform's default behavior of selecting one based on the resource type name.






## Lifecycle Meta argument

- Some details of the default resource behavior can be customized using the special nested lifecycle block within a resource block body.

There are 4 argument available within lifecycle block:
#### create_before_destory - new replacement object is created first and the prior object is destoryed after the replacement is created.
#### prevent_destory - to reject with an error any plan that would destroy the infrastructure object associated with the resource.
#### ignore_changes - ignore certain changes to the live resource that does not match the configuration.
#### replace_triggered_by - replace the resource when any of the referenced items changes.

### Create before destory

resource "aws_instance" "web1" {
    ami = ami-qweqdcda212e3de
    instance_type = t2.micro

    lifecycle {
        create_before_destory = true
    }
}

### Prevent destroy

resource "aws_instance" "web1" {
    ami = ami-qweqdcda212e3de
    instance_type = t2.micro

    lifecycle {
        prevent_destory = true
    }
}

- This can be used as a measure of safety against the accidental replacement of object that may be costly to reproduce. such as a database instance.
- Since the argument must be present in the configuration for the protection to apply, note that this settings does not prevent the remote object from being destroyed if the resource block were removed from configuration entirely. 

### Ignore Changes

resource "aws_instance" "web1" {
    ami = ami-qweqdcda212e3de
    instance_type = t2.micro

    tags {
        name = web1
    }

    lifecycle {
        ignore_changes = [tags]
    }
}

- In case where settings of a remote object is modified by processes outside of Terraform, the Terraform would attempt to "fix" on the next run. 
- In order to change this behavior and ignore the manually applied change, we can make use of ignore_changes argument under lifecycle.
- Keyword 'all' can be used to ignore all changes.






## for_each in Terraform

- for_each makes use of map/set as an index value of the created resource.

resource "aws_iam_user" "user" {
    for_each = toset(["user1","user2","user3"])
    name = each.key
}

- In blocks where for_each is set, an additional each object is available.
- This object has two attributes:
    - each.key - the key map or set
    - each.value - the value 






## Terraform Registry
- Terraform registry is a repository of modules written by the terraform community.
- The registry can help you get started with terraform more quickly

### Verified modules
- Within Terraform Registry you can find verified modules that are maintained by various third party vendors. These modules are available for various resources like AWS VPC, RDS, ELB and others.
- Verified modules are reviewd by Hashi Corp and actively maintained by contrbutors to stay up-to-date and compatible with both Terraform and their respective providers.
- The blue verification badge appears next to modules that are verified.
- Modules verification is currently a manual process restricted to a small group of trusted HashiCorp partners.

### Using Registry Module in Terraform
- To use Terraform Registry module with the code, we can make use of the source argument that contains the module path

EG:
module "ec2-instance" {
    source = "terraform-aws-modules/ec2-instance/aws"
    version = "2.13.0"
    # insert the 10 required variables here
}

### Publishing Registry Module
- Anyone can publish and share modules on the terraform registry.
- Publish modules support versioning, automatically generate documentation, allow browsing version histories, show examples and README and more 
- Standard module structure is a file and directory layout that is recommended for reusable modules distributed in seperate repositories
- Requirements: 
    - GitHub: module must be in a github and must be public repo. 
    - Named: module repository must be in three part name format "terraform-<provider>-<name>"
    - Repository Discription: GitHUb repo description is used to populate the short description of the module
    - Standard module structure: module must adhere standard module structure of files & folders
    - x.y.z tags for releases: Release tag names must be a semantic version eg: v1.0.1

## Module Sources
- The source argument in a module block tells Terraform where to find the source code for the desired child module

    * Local Path = A local path must begin with ./ or ../ to indicate that local path is intended
    * Git = Arbitrary Git repositories can be used by prefixing the address with the special git:: prefix. After this prfix any valid Git URI can be specified to select of the protocols supported by git. Using ref argument we can use specific branch






## Terraform Workspace

- Terraform allows us to have multiple workspaces, with each of the workspace we can have different set of environment variable associated.

```terraform workspace``` - to create, delete and switch workspace
- Sub commands delete, list, new, select, show