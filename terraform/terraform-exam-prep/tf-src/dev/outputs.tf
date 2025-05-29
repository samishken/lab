output "instance_ip_address" {
  description = "The public IP address of the instance"
  value       = aws_instance.my_server.public_ip
}