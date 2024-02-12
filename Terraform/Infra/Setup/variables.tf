variable "vpc_id" {
  type        = string
  description = "input vpc id for ec2 instance"
}

variable "subnet_id" {
  type        = string
  description = "input subnet id for ec2 instance"
}

variable "sg_ports" {
  type        = list(number)
  description = "provide list of ports to be opened"
  default     = [22]
}

variable "instance_type" {
  type        = string
  description = "input instance type for ec2 instance"
  default     = "t2.micro"
}

variable "disk_size" {
  type        = number
  description = "input disk size for ec2 instance"
  default     = "8"
}

variable "server_name" {
  type        = string
  description = "Name Tag for ec2 instance"
}