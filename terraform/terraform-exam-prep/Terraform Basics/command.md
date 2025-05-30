# Terraform commands

- `terraform init`
- `terraform plan`
- `terraform fmt`
- `terraform validate`
- `terraform apply`
- `terraform destroy`
- `terraform apply -var-file=vars.tfvars`   # is used to set the variables for the dev environment
- `-var-file=vars.tfvars`: This flag tells Terraform to load variable values from the file `vars.tfvars`. This file is typically written in HCL (HashiCorp Configuration Language) or JSON format and defines values for input variables used in the configuration.
- `terraform plan -var instance_type="t2.medium"` variable precedence