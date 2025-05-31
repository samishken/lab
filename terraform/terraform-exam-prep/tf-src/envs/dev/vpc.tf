module "exam-prep-vpc" {
  source = "git::https://github.com/samishken/lab.git//terraform/terraform-exam-prep/tf-src/modules/vpc"
  # source = "../../modules/vpc"  # source should point to our custome vpc module

  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  tags = {
    Terraform   = "true"
    Name        = "${local.environment}-${local.project_name}-exam-prep-vpc"
    Project     = "${local.project_name}"
    Environment = "${local.environment}"
  }
}