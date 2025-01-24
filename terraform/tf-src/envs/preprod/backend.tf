terraform {
  backend "s3" {
    bucket         = "terraform-state-preprod"
    key            = "preprod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-preprod"
    encrypt        = true
  }
}
