output "instance_id" {
  value = aws_instance.gbfs_monitoring.id
}

output "public_ip" {
  value = aws_instance.gbfs_monitoring.public_ip
}
