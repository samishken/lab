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
  subnet_id              = aws_subnet.pub_sub1.id
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  # user_data = <<-EOF
  #             #!/bin/bash
  #             set -ex
  #             # Install Docker
  #             sudo apt-get update
  #             sudo apt-get install -y docker.io
  #             sudo systemctl enable docker
  #             sudo systemctl start docker
  #             sudo usermod -aG docker ubuntu

  #             # Install kubectl
  #             curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  #             sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

  #             # Install Terraform
  #             sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
  #             wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
  #             echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
  #             sudo apt update
  #             sudo apt-get install terraform
  #         EOF

  tags = {
    Name = "devops-project"
  }
}