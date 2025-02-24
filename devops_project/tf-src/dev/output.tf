output "security_group_public" {
  value = aws_security_group.ec2_sg.id
}

output "public-subnet1" {
  value = aws_subnet.pub_sub1.id
}
output "public-subnet2" {
  value = aws_subnet.pub_sub2.id
}

output "vpcid" {
  value = aws_vpc.vpc.id
}

output "instance_public_ip" {
  value = aws_instance.devops-project.public_ip
}
