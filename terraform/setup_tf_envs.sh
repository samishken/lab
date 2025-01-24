#!/bin/bash

# Define base directory
BASE_DIR="tf-src"
MODULES_DIR="$BASE_DIR/modules"
ENVS_DIR="$BASE_DIR/envs"
GLOBAL_DIR="$BASE_DIR/global"

# Define environments
ENVIRONMENTS=("stage" "preprod" "prod")

# Create base directories
mkdir -p $MODULES_DIR $GLOBAL_DIR

# Create reusable module directories
mkdir -p $MODULES_DIR/{networking,compute,storage,security}

# Create global configuration files
cat <<EOF > $GLOBAL_DIR/provider.tf
provider "aws" {
  region = "us-east-1"
}
EOF

cat <<EOF > $GLOBAL_DIR/variables.tf
variable "aws_profile" {}
EOF

# Loop through environments and create structure
for ENV in "${ENVIRONMENTS[@]}"; do
    ENV_DIR="$ENVS_DIR/$ENV"
    mkdir -p $ENV_DIR

    # Create backend configuration
    cat <<EOF > $ENV_DIR/backend.tf
terraform {
  backend "s3" {
    bucket         = "terraform-state-$ENV"
    key            = "$ENV/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-$ENV"
    encrypt        = true
  }
}
EOF

    # Create provider configuration
    cat <<EOF > $ENV_DIR/provider.tf
provider "aws" {
  region  = "us-east-1"
  profile = "$ENV-account-profile"
}
EOF

    # Create main.tf (example infrastructure)
    cat <<EOF > $ENV_DIR/main.tf
module "networking" {
  source = "../../modules/networking"
}

module "compute" {
  source = "../../modules/compute"
}

module "storage" {
  source = "../../modules/storage"
}

module "security" {
  source = "../../modules/security"
}
EOF

    # Create variables.tf
    cat <<EOF > $ENV_DIR/variables.tf
variable "aws_profile" {}
variable "vpc_cidr" {}
EOF

    # Create terraform.tfvars
    cat <<EOF > $ENV_DIR/terraform.tfvars
aws_profile = "$ENV-account-profile"
vpc_cidr    = "10.${RANDOM:0:1}.0.0/16"
EOF

    # Create outputs.tf
    cat <<EOF > $ENV_DIR/outputs.tf
output "aws_region" {
  value = "us-east-1"
}
EOF
done

echo "Terraform environment setup completed in $BASE_DIR"

