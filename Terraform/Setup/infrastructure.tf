# data from AWS
data "aws_ami" "amazon2-linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-kernel*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

data "aws_iam_policy" "AmazonSSMManagedInstanceCore" {
  arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}
data "aws_iam_policy" "AmazonEC2RoleforSSM" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
}
data "aws_iam_policy" "CloudWatchActionsEC2Access" {
  arn = "arn:aws:iam::aws:policy/CloudWatchActionsEC2Access"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Resource section starts here

## Local resources
resource "tls_private_key" "tls-private-key" {
  algorithm = "RSA"
}

resource "local_file" "private-key-file" {
  content         = tls_private_key.tls-private-key.private_key_pem
  filename        = "jenkins.pem"
  file_permission = "0600"
}

## AWS resources
resource "aws_key_pair" "jenkins-server-key" {
  key_name   = "jenkins-server-key"
  public_key = tls_private_key.tls-private-key.public_key_openssh
}

resource "aws_security_group" "jenkins_sg" {
  name        = "jenkins-server-sg"
  description = "security group for jenkins server"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.sg_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_role" "jenkins-server-role" {
  name = "jenkins-server-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
  inline_policy {
    name = "TagRootVolumePolicy"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action   = "ec2:Describe*"
          Effect   = "Allow"
          Resource = "*"
        },
        {
          Action   = "ec2:CreateTags"
          Effect   = "Allow"
          Resource = "*"
        },
      ]
    })
  }
  managed_policy_arns = [data.aws_iam_policy.AmazonSSMManagedInstanceCore.arn, data.aws_iam_policy.AmazonEC2RoleforSSM.arn, data.aws_iam_policy.CloudWatchActionsEC2Access.arn]
}

resource "aws_iam_instance_profile" "EC2InstanceProfile" {
  name = "EC2InstanceProfile"
  path = "/"
  role = aws_iam_role.jenkins-server-role.name
}

resource "aws_instance" "jenkins-server" {
  instance_type          = var.instance_type
  ami                    = data.aws_ami.amazon2-linux.id
  vpc_security_group_ids = [aws_security_group.jenkins_sg.id]
  subnet_id              = var.subnet_id
  iam_instance_profile   = aws_iam_instance_profile.EC2InstanceProfile.name
  key_name               = aws_key_pair.jenkins-server-key.key_name
  root_block_device {
    volume_size = var.disk_size
  }
  tags = {
    Name = var.server_name
  }
}

###### outputs #####

output "jenkins_instance_id" {
  value = aws_instance.jenkins-server.id
}
output "jenkins_public_ip" {
  value = aws_instance.jenkins-server.public_ip
}