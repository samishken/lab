locals {
  ingress = [{
    port        = 443
    description = "Allow HTTPS traffic"
    protocol    = "tcp"
    }, {
    port        = 80
    description = "Allow HTTP traffic"
    protocol    = "tcp"
    }, {
    port        = 22
    description = "Allow SSH traffic"
    protocol    = "tcp"
  }]
}
locals {
  egress = [{
    port        = 0
    description = "Allow all outbound traffic"
    protocol    = "-1"
  }]
}

resource "aws_security_group" "myserver_sg" {
  vpc_id      = module.exam-prep-vpc.vpc_id
  name        = "${local.environment}-${local.project_name}-sg"
  description = "Security group for my server"
  tags = {
    Terraform   = "true"
    Environment = "${local.environment}"
    Project     = "${local.project_name}"
  }

  dynamic "ingress" {
    for_each = local.ingress
    content {
      description      = ingress.value.description
      from_port        = ingress.value.port
      to_port          = ingress.value.port
      protocol         = ingress.value.protocol
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  }
  dynamic "egress" {
    for_each = local.egress
    content {
      description      = egress.value.description
      from_port        = egress.value.port
      to_port          = egress.value.port
      protocol         = egress.value.protocol
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  }
}