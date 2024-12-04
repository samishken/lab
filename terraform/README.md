# Terraform Notes

#### Providers
- Providers are plugins for Terraform that extend it with support for interacting with various external systems.

Any service with an API can be managed by Terraform.  So to do this you must use what's called a PROVIDER.  
A provider essentially translates the APIs create, read, update, and delete operations into a standard that Terraform can understand.
A Terraform provider is a plugin that acts as an interface between Terraform and an external service or platform, 
allowing Terraform to manage resources on that platform by interacting with its API, 
essentially enabling the creation, reading, updating, and deletion (CRUD) of resources across various cloud providers and 
other infrastructure services through a single, standardized configuration language

#### Terraform Lock file
- the Terraform lock file ensures that the same provider version is used across different systems and different Terraform runs.
- The lock file guarantees a consistent install across machines. Your Package Manager will use the lock file to resolve and install modules. 
- The lock file locks the specific version, location, and integrity hash for every package.

###### Terraform init ".terraform"
- Initialize the directory
- initializes a working directory containing Terraform configuration files

###### Terraform Plan
- a Terraform CLI command that previews the changes that Terraform will make to an infrastructure

##### Terraform apply
- applies infrastructure changes specified in an Infrastructure-as-Code (IaC) configuration to the actual infrastructure
- The terraform apply command creates, updates, or deletes infrastructure resources to match the new state in the IaC.

###### Statefile
- Statefile is the state of the resources that we've deployed, sets it apart from other deployment tools, such as Ansible.
- This state is a file that needs to be stored somewhere.
- It defaults to our local file system, but we can also store it in Terraform Cloud, Amazon S3, and
- HTTP server, or many other potential locations... 

- It contains everything that Terraform needs to manage our infrastructure.
- The state is created as soon as we run a Terraform apply and it keeps it up to date any time we use the apply or refresh commands.
<br>
------  Statefile storage locations are known as BACKENDS.
------- 


###### terraform show
- shows current state
- output in json "terraform show -json | jq" 

###### terraform state list
- lists all resources in statefile

###### terraform state show 
- "terraform state show github_repository.mtc_repo"
- shows all the resources of mtc_repo


###### terraform console
- "terraform console -state="../state/terraform.tfstate"
- Starts an interactive console for experimenting with Terraform interpolations. (works like python)
- we can get detailed information about a resource so that we can interpolate  
- "mtc-repo-${random_id.random.dec}"


###### terraform count
- With Count, we can simply tell Terraform how many copies of a resource we want

##### Output
- a feature of Terraform CLI that allow users to access and display data from their infrastructure configurations

##### Splat expression
- expression to help structure the outputs that we create to display everything we need.
- a shorthand way to perform common operations, 
