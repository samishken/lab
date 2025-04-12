# variable "repo_name" {
#   type        = string
#   default     = "home-lab-project-ecr"
#   description = "ECR repo to store a Docker image"
# }

variable "cluster_name" {
  description = "Name of the ECR"
  default     = "home-lab-project-ecr"
  type        = string
}