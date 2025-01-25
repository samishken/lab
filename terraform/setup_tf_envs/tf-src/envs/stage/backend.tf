terraform {
  backend "s3" {
    bucket = "terraform-state-"
    key    = "stage/terraform.tfstate"
    region = "us-east-1"
  }
}
