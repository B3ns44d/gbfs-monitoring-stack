provider "aws" {
  region = var.region
}

terraform {
  backend "s3" {
    bucket = var.bucket
    key    = "terraform.tfstate"
    region = var.region
  }
}
