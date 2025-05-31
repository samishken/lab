# Terraform State
### What is State?
- A particular condition of cloud resources at a specific time.

eg. We expect there to be a Virtual Machine running CentOS on AWS with a compute type of t2.micro.

### How does Terraform preserve state?

When you provision infrastructure via Terraform it will create a state file named `terraform.tfstate`

This `state file is a JSON data structure` with a one-to-one mapping from `resource instances` to `remote objects`

Configuration files:

- - - main.tf
- - - variables.tf
- - - terraform.tfvars

Terraform apply command
- Terraform API
- Remote objects
- State file => `terraform.tfstate`
---

terraform CLI commands

`terraform state list` => List resources in the state

`terraform state show`=> Show a resource in the state

`terraform state rm` => Remove instances from the state

`terraform state mv` => Move an item in the state. We can update the info inside the state file. Allows us to
- - - - rename existing resources
- - - - move a resource into a module
- - - - move a module into a module

`terraform state pull` => Pull current remote state and output to stdout

`terraform state push` => Update remote state from a local state

`terraform state replace-provider` => Replace provider in the state


Terraform State Backups file
`terraform.tfstate.backup`