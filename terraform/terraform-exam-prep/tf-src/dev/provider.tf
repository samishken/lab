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
    # google = {
    #   source = "hashicorp/google"
    #   version = "6.37.0"
    # }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "google" {
  alias  = "west"
  region = "us-west-1"
}