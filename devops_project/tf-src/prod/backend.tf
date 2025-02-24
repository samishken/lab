terraform {
  backend "s3" {
    bucket = "terraform-state-devops-project-samboo"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}

