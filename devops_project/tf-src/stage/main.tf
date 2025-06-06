module "vpc_stage" {
  source = "./modules/vpc"

  vpc_cidr             = var.vpc_cidr
  availability_zones   = var.availability_zones
  private_subnet_cidrs = var.private_subnet_cidrs
  public_subnet_cidrs  = var.public_subnet_cidrs
  cluster_name    = var.cluster_name  
}

module "eks" {
  source = "./modules/eks"

  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version
  vpc_id          = module.vpc_stage.vpc_id
  subnet_ids      = module.vpc_stage.private_subnet_ids
  node_groups     = var.node_groups
}

module "ecr" {
  source = "./modules/ecr"

  repo_name = var.ecr_repo_name
}