module "network" {
  source            = "./modules/network"
  vpc_cidr_block    = var.vpc_cidr_block
  subnet_cidr_block = var.subnet_cidr_block
  env_name          = var.env_name
}

module "security_group" {
  source   = "./modules/security_group"
  vpc_id   = module.network.vpc_id
  env_name = var.env_name
}

module "ec2" {
  source            = "./modules/ec2"
  ami_id            = var.ami_id
  instance_type     = var.instance_type
  subnet_id         = module.network.subnet_id
  security_group_id = module.security_group.security_group_id
  key_pair          = var.key_pair
  env_name          = var.env_name
  depends_on        = [
    module.network,
    module.security_group
  ]
}
