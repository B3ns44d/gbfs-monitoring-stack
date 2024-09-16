variable "region" {
  description = "AWS region"
  default     = "eu-north-1"
  type        = string
}

variable "bucket" {
  description = "S3 bucket name to store Terraform state"
  default     = "gbfs-terraform-state"
  type        = string
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
  type        = string
}

variable "subnet_cidr_block" {
  description = "CIDR block for the subnet"
  default     = "10.0.1.0/24"
  type        = string
}

variable "env_name" {
  description = "Environment name (e.g., dev, prod)"
  default     = "dev"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for EC2 instance"
  default     = "ami-0c6da69dd16f45f72"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.micro"
  type        = string
}

variable "key_pair" {
  description = "Key pair for SSH access"
  type        = string
}
