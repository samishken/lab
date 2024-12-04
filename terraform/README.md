

#### Provider

Any service with an API can be managed by Terraform.  So to do this you must use what's called a PROVIDER.  
A provider essentially translates the APIs create, read, update, and delete operations into a standard that Terraform can understand.
A Terraform provider is a plugin that acts as an interface between Terraform and an external service or platform, 
allowing Terraform to manage resources on that platform by interacting with its API, 
essentially enabling the creation, reading, updating, and deletion (CRUD) of resources across various cloud providers and 
other infrastructure services through a single, standardized configuration language


###### Terraform init ".terraform"
- Initialize the directory
- initializes a working directory containing Terraform configuration files

###### Terraform Plan
- a Terraform CLI command that previews the changes that Terraform will make to an infrastructure

##### Terraform apply
- applies infrastructure changes specified in an Infrastructure-as-Code (IaC) configuration to the actual infrastructure
- The terraform apply command creates, updates, or deletes infrastructure resources to match the new state in the IaC.

###### Statefile
- Statefileß is the state of the resources that you've deployed, sets it apart from other deployment tools, such as Ansible.
- This state is a file that needs to be stored somewhere.
- It defaults to your local file system, but you can also store it in Terraform Cloud, Amazon S3, and
- HTTP server, or many other potential locations... 
<br>
------  Statefile storage locations are known as BACKENDS.
------- 
