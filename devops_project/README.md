# DevOps End-to-End Project

- Clone this to aws (https://github.com/iam-veeramalla/ultimate-devops-project-demo)
- Notes - https://github.com/iam-veeramalla/ultimate-devops-project-aws

Steps to start this project:
1) deploy infra using terraform (run necessary scripts) <br>
2) deploy service account <br> 
3) deploy deployment manifest files <br>
4) deploy ALB Ingress controller <br>
- - setup IAM OIDC provider: connects pods inside the cluster to elastic loadbalancer which are outside the cluster
- - Deploy ingress
5) setup route53
6) create CICD to deploy the application.
7) ArgoCD

#### IAM 
- Creates users, usergroups, roles, policies
- RBAC
- - Authentication: Access to enter to a service (Users & usergroups)
- - Authorization: permissions to access different services/resources. (roles & policies)

#### Terraform commands
- terraform fmt
- terraform state list
- terraform output
- terraform validate


#### EC2
- Install kubectl, terraform, docker
- Increase volume size to 30GB
- run the following commands to fix disk size issue
- - `df -h`
- - `lsblk`
- - `sudo growpart /dev/xvda 1`
- - `sudo resize2fs /dev/xvda1`
- - `df -h`

#### docker compose
- `docker compose up`
- `docker compose up -d`
- Implement Docker lifecycle