resource "aws_security_group" "ec2_sg" {
  name        = "devops-project-preprod-sg"
  description = "allow-ssh"
  vpc_id      = aws_vpc.vpc.id

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Acesse via SSH de qualquer lugar
  }
  ingress {
    from_port   = 31000
    to_port     = 31000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Acesse vault ui
  }
}


