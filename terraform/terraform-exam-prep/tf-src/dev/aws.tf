module "exam-prep-vpc" {
  source = "terraform-aws-modules/vpc/aws"

  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = "dev-${local.project_name}"
  }
}

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


resource "aws_instance" "my_server" {
  for_each = {
    "nano"  = "t2.nano"
    "micro" = "t2.micro"
    "small" = "t2.small"
  }
  ami           = data.aws_ami.ubuntu.id
  instance_type = each.value
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }

  provisioner "remote-exec" {
    inline = [
      "echo ${self.private_ip} >> /home/ubuntu/private_ips.txt"
    ]
    # connection {
    #   type = "ssh"
    #   user = "ubuntu"
    #   #private_key = "${file("home/shaile/ssh/lenovo.pub")}"
    #   host = self.public_ip
    # }
  }

  # allows you to change what happens to resources e.g. create, update, destroy.
  lifecycle {
    prevent_destroy = false # true: prevents the instance from being destroyed.  This is useful for exam prep to avoid accidental deletions
    ignore_changes = [
      tags["Environment"], # Terraform will ignore manual changes to this tag
      user_data,           # Also ignore changes to user_data
    ]
  }
  tags = {
    Name        = "MyServer-${each.key}"
    Environment = "MyServer-${local.project_name}"
  }

}

# Check if the instance is running or not
# Note: null_resouce is now terraform_data
resource "null_resource" "status" {
  for_each = aws_instance.my_server
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${each.value.id}"
  }
  depends_on = [
    aws_instance.my_server
  ]
}