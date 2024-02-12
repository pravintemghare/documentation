## Variables in Terraform

- Repeated static values can create more work in the future.
- We can have central source from which we can import the values from.
- File can be named as variable.tf

variable "variable_name" {
    default = "some_value"
}

- Reference in main.tf file

resource local_file "file1" {
    filename = var.variable_name
}



- Variables in Terraform can be assigned values in multiple ways:
    - Environment variables
    - Command Line flags
    - From a file
    - Variable Defaults

- To provide variables from command line "terraform plan -var="variable_name=some_value""

- To provide variables from a file create file "terraform.tfvars" provide variables in this file.
    variable_name="some_value"
- To use a custome file we need to specify file name in command line "terraform plan -var-file="custom.tfvars""

- To specify variable using environment variable
    - Windows: setx TF_VAR_variablename some_value
    - Linux: export TF_VAR_variablename="somevalue"






## Variable Data Types

- The type argument in a variable block allows you to restrict the type of value that will be accepted as the value for a variable

variable "variablename" {
    type = string
}

- If no type constraint is set then a value of any type is accepted.

- Variable Data type:
    - string = (sequence of unicode characters representing some text "test","hello")
    - number = (only whole numbers allowed "100" "200")
    - list = (sequential list of values identified by their position Stats with 0 ["mumbai","pune","banglore"])
    - map = (a group of values identified by named labels {name="jhon",age="20"})

## Feteching data from Maps & Lists

resource resource_name "test" {
    parameter = var.variablename["name1"]
}

variable variablename {
    type = map
    default = {
        name1 = "tom"
        name2 = "dick"
        name3 = "harry"
    }
}

## Data sets

- SET is used to store multiple items in a single variable
- SET items are unordered and no duplicates allowed
    demoset = {"apple", "banana", "Watermellon"}
- ```to set``` function will convert the list of values to SET

##############################################

resource resource_name "test" {
    parameter = var.variablename["2"]
}

variable variablename {
    type = list
    default = [tom,dick,harry]
}






## Count & Count Index

- The count parameter on resources can simplify configurations and let you scale resources by simply incrementing a number
- With count parameter we can simply specify the count value and the resource can be scaled accordingly.

resource "aws_instance" "web1" {
    ami = "ami-23r23r23fnjew91"
    instance_type = "t2.micro"
    count = 2
}

### Count Index
- In resource blocks where count is set, an additional count object is available in expressions, so you can modify the configuration of each instance.

count.index - The distinct index number (starting with 0) corresponding to this instance. 

resource "aws_iam_user" "testuser" {
    name = "testuser.${count.index}"  
    count = 5
    path = /system/
}

variable elb_name {
    type = list
    default = [qa,stage,prod]
}

resource aws_alb alb {
    name = var.elb_name[count.index]
    count = 3
}




## Conditional Experessions
- A conditional experession uses the value of a bool experession to select one of two values.
- Syntax for conditional expression:
    condition ? true_val : false_val
- If condition is true then the result is true_val. If condition is false then the result is false_val

variable istest {}

resource "aws_instance" "dev" {
    ami = "ami-adadcq2f3qveqe"
    instance_type = "t2.micro"
    count = var.istest == true ? 1 : 0
}

resource "aws_instance" "prod" {
    ami = "ami-adadcq2f3qveqe"
    instance_type = "m5.large"
    count = var.istest == false ? 1 : 0
}


To assign variable create a new file variables.tf

Sample:
    variable "filename" {
        default = "/root/testfile.txt"
        type = string
        description = "some information about variable"
    }

to use it in main.tf

resource "local_file" "test" {
    filename = `var.filename`
}

We can use type as string, number, bool, any(default)
additional type: list, map, object & tuples

list(string)
list(number)

to use list 
default = ["Mr", "Mrs", "Sir"]
prefix = var.var_name[0]

to use map - key value pair
default = {
    "one" = "1"
}
content = var.var_name["one"] - matching key

to use sets - cannot have duplicate elements
default = ["apple", "manago"]

to use objects
type = object({
    name = string
    color = string
})

### Input variable using variable file

terraform apply -var "var1=one" -var "var2=two"

export TF_VAR_filename="root/text.txt"

terraform.tfvars file extension supported terraform.tfvars.json *.auto.tfvars *.auto.tfvars.json
filename = "/root/test.txt"
lenght = "2"

First - the export variable
Second - terraform.tfvars
Third - variable.auto.tfvars
Fouth - Command line variables