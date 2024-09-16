variable "region" {
  description = "AWS region"
  type        = string
}

variable "bucket" {
  description = "S3 bucket name to store Terraform state"
  type        = string
}

variable "key" {
  description = "Path to store Terraform state within the S3 bucket"
  type        = string
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "subnet_cidr_block" {
  description = "CIDR block for the subnet"
  type        = string
}

variable "env_name" {
  description = "Environment name (e.g., dev, prod)"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "key_pair" {
  description = "Key pair for SSH access"
  type        = string
}
