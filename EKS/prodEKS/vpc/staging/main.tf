terraform {
  backend "s3" {
    bucket = "terraformaws11-samboo"
    key    = "aws-terraform-vpc.tfstate"
    region = "us-east-1"
  }
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

resource "aws_vpc" "main" {
 cidr_block = "10.0.0.0/16"
 
 tags = {
   Name = "${var.environment}-vpc"
 }
}

resource "aws_subnet" "pubsub1" {
    vpc_id = aws_vpc.main.id
    cidr_block = "10.0.1.0/24"
    map_public_ip_on_launch = true
    availability_zone = "us-east-1a"
    
    tags = {
        Name = "pubsub1-${var.environment}"
    }
}

resource "aws_subnet" "pubsub2" {
    vpc_id = aws_vpc.main.id
    cidr_block = "10.0.2.0/24"
    map_public_ip_on_launch = true
    availability_zone = "us-east-1b"

    tags = {
        Name = "pubsub2-${var.environment}"
    }
}

resource "aws_subnet" "privsub1" {
    vpc_id = aws_vpc.main.id
    cidr_block = "10.0.3.0/24"
    availability_zone = "us-east-1c"

    tags = {
        Name = "privsub1-${var.environment}"
    }
}

resource "aws_subnet" "privsub2" {
    vpc_id = aws_vpc.main.id
    cidr_block = "10.0.4.0/24"
    availability_zone = "us-east-1d"

    tags = {
        Name = "privsub2-${var.environment}"
    }
}

resource "aws_internet_gateway" "gw" {
    vpc_id = aws_vpc.main.id
 
    tags = {
        Name = "igw-${var.environment}"
    }
}

resource "aws_route_table" "rt" {
 vpc_id = aws_vpc.main.id
 
 route {
   cidr_block = "0.0.0.0/0"
   gateway_id = aws_internet_gateway.gw.id
 }
}

resource "aws_route_table_association" "rt_pubsub1" {
  subnet_id      = aws_subnet.pubsub1.id
  route_table_id = aws_route_table.rt.id
}

resource "aws_route_table_association" "rt_pubsub2" {
  subnet_id      = aws_subnet.pubsub2.id
  route_table_id = aws_route_table.rt.id
}