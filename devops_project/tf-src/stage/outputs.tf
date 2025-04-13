output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc_stage.vpc_id
}

output "ecr_repo_name" {
  description = "ECR repository name"
  value       = module.ecr.ecr_repo_name
}