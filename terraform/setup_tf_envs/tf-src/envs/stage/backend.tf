terraform {
  backend "s3" {
    bucket = "terraform-state-dev-samboo"
    key    = "stage/terraform.tfstate"
    region = "us-east-1"
  }
}

# devops-infra
# _9D-@YAJCzruU2F 