terraform {
  backend "s3" {
    bucket         = "terraform-state-stage"
    key            = "stage/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-stage"
    encrypt        = true
  }
}
