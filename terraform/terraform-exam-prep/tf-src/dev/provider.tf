# terraform {
#   backend "s3" {
#     bucket = "terraform-state-dev-samboo"
#     key    = "dev/terraform-exampro.tfstate"
#     region = "us-east-1"
#   }
# }

terraform {
  cloud {
    organization = "terraform-exam-prep-samboo"
    workspaces {
      name = "getting-started"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.0.0-beta2"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
}