variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "subnet_id" {
  description = "ID of the subnet"
  type        = string
}

variable "security_group_name" {
  description = "Name of the security group"
  type        = string
}

variable "key_pair" {
  description = "Key pair for SSH access"
  type        = string
}

variable "env_name" {
  description = "Environment name (dev, prod)"
  type        = string
}
