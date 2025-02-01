terraform {
  backend "s3" {
    bucket = "terraform-state-dev-samboo"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}

