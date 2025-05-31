# Terraform Troubleshooting
### There are four types of errors you can encounter with Terraform:

---
## [Easy to Solve]

### Language errors
Terraform encounters a syntax error in your configuration for the Terraform or HCL Language

- - - - terraform fmt
- - - - terraform validate
- - - - terraform version

### State errors
Your resources state has changed from the expected state in your configuration file

- - - - terraform refresh
- - - - terraform apply
- - - - terraform –replace flag

---
## [Harder to Solve]

### Core errors
- A bug has occurred with the core library
- - - - TF_LOG
- - - - Open Github Issue

### Provider errors
- The provider’s API has changed or does not work as expected due to emerging edge cases
- - - - TF_LOG
- - - - Open Github Issue


### TF_LOG environment
Terraform has detailed logs which can be enabled by setting the TF_LOG environment variable to:
- - - - TRACE
- - - - DEBUG
- - - - INFO
- - - - WARN
- - - - ERROR
- - - - JSON — outputs logs at the TRACE level or higher, and uses a parseable JSON encoding as the formatting.

- Logging can be enabled separately: takes the same options as TF_LOG
- - - - TF_LOG _CORE
- - - - TF_LOG _PROVIDER

Choose where you want to log with `TF_LOG _PATH`

- `TF_LOG=trace terraform apply`
- `TFLOGCORE=trace terraform apply`
- Save log: `TFLOG=trace TFLOG_PATH=terraform.log terraform apply`
- `TFLOGPROVIDER=trace terraform apply`

