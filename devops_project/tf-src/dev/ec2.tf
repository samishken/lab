data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "devops-project" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.large"
  key_name               = "dev-account-lenovo"
  #subnet_id              = aws_subnet.pub_sub1.id
  vpc_security_group_ids = [aws_security_group.ec2_sg_dev.id]

  root_block_device {
    volume_type = "gp3"
    volume_size = 30 # Size in GB
  }

  # ToDO: Add user_data to install docker, terraform, ansible, kubectl
  # user_data = <<-EOF
  #              EOF

  tags = {
    Name = "devops-project-dev"
  }
}