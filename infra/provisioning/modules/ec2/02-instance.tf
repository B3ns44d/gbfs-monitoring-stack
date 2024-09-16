resource "aws_instance" "gbfs_monitoring" {
  lifecycle {
    ignore_changes = [
      security_groups
    ]
  }
  ami                         = var.ami_id
  instance_type               = var.instance_type
  subnet_id                   = var.subnet_id
  key_name                    = var.key_pair
  security_groups             = [var.security_group_name]
  associate_public_ip_address = true
  tags = {
    Name = "${var.env_name}-gbfs-monitoring-instance"
  }
}