resource "aws_instance" "linux-ec2" {
  ami           = "ami-0df8c184d5f6ae949"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.ec2_sg.name]
  key_name        = "dev-account-lenovo"

  tags = {
    Name = "Test-Amazon-Linux"
  }
}

resource "aws_instance" "hashicorp_vault" {
  ami             = "ami-04b4f1a9cf54c11d0"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.ec2_sg.name]
  key_name        = "dev-account-lenovo"

  tags = {
    Name = "HashiCorp_Vault"
  }
}

resource "aws_security_group" "ec2_sg" {
  name        = "main-sg"
  description = "ssh-to-ec2"
  
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
    from_port   = 8200
    to_port     = 8200
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Acesse vault ui
  }
}