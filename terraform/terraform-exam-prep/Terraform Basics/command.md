# Terraform commands

- `terraform init` -> ` .terraform.lock.hcl` & `.terraform` directory. 
- `terraform init upgrade`
- `terraform plan`: Terraform command creates an `execution plan` (aka Terraform Plan). 
- `terraform plan -out=FILE`: You can generate a saved plan file which you can then pass along to terraform apply
- `terraform fmt` (`terraform fmt --diff`): rewrites Terraform configuration files to a standard format and style
- `terraform validate`: rewrites Terraform configuration files to a standard format and style
- `terraform console`: an interactive shell for evaluating Terraform expressions
- `terraform apply`: Terraform apply command executes the actions proposed in an execution plan
- `terraform apply –auto-approve` flag will automatically approve the plan.
- `terraform destroy`
- `terraform apply -var-file=vars.tfvars`   # is used to set the variables for the dev environment
- `-var-file=vars.tfvars`: This flag tells Terraform to load variable values from the file `vars.tfvars`. This file is typically written in HCL (HashiCorp Configuration Language) or JSON format and defines values for input variables used in the configuration.
- `terraform plan -var instance_type="t2.medium"` variable precedence
- `terraform apply -refresh-only` Re-evaluate the current infrastructure state from the real resources (refresh)


# Built in functions
- `count` - more study
- `for_each` - more study
- `depends_on` 
- `Alias` - more study



# Terraform Init
- 