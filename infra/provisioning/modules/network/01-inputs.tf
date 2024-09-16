variable "vpc_cidr_block" {
  description = "CIDR block for VPC"
  type        = string
}

variable "subnet_cidr_block" {
  description = "CIDR block for Subnet"
  type        = string
}

variable "env_name" {
  description = "Environment name (dev, prod)"
  type        = string
}
