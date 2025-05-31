# Manage Resource Drift
Drift (Configuration or Infrastructure) is when your expected resources are in a different state than your expected state

We can resolve Drift in three ways in Terraform:

## Replacing Resources
- When a resource has become damaged or degraded that cannot be detected by Terraform we can use the `–replace` flag
- It is recommended in 0.15.2+ to use the `-replace` flag and providing a resource address
- The replace flag is available on plan and apply
- The replace flag appears to only work for a single resource
- `terraform apply -replace="aws_instance.example[0]`

## Importing Resources 
- When an approved manual addition of resource needs to be added to our state file
- We use the `import` command.

## Refresh State
- When an approved manual configuration of a resource has changed or removed
- We use the `–refresh-only` flag to reflect the changes in our state file

## Terraform Import
- `terraform import RESOURCE_ADDRESS ID` : The terraform import command is used to import existing resources into Terraform
- One resource at a time

