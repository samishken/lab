# Terraform Backends
- Each Terraform configuration can specify a backend, which defines where and how operations are performed, where state snapshots are stored

## Terraform's backends are divided into two types:

### Standard backends
- only store state
- does not perform terraform operations eg. Terraform apply
- - - - To perform operations you use the CLI on your local machine
- `third-party backends` are Standard backends e.g. AWS S3

### Enhanced backends
- can both store state and perform terraform operations

### Enhanced backends are subdivided further:
* * * local – files and data are stored on the local machine executing terraform commands
* * * remote – files and data are stored in the cloud eg. Terraform Cloud

### Local Backends
The local backend:
- stores state on the local filesystem
- locks that state using system APIs
- performs operations locally

`By default`, you are using the backend state when you have not specified backend

You specify the backend with argument local, and you can change the path to the local file and working_directory

You can set a backend to reference another state file so you can read its outputted values.

### Remote Backend
A Remote backend uses the Terraform platform which is either:
- Terraform Cloud
- Terraform Enterprise
With a remote backend when terraform apply is performed via the CLI

The Terraform Cloud Run Environment is responsible for executing the operation

Because the Terraform Cloud Run Environment is executing the command. Your provider credentials `need to be configured` in Environment Variabels in Terraform Cloud

When using a remote backend you need to set a Terraform Cloud Workspaces

You can set a single workspace via name

You can set multiple workspaces via prefix

On terraform apply you will have to choose which workspace you want to apply the operation

Setting both name and prefix will result in an error.

### Cloud Backend
When using Terraform Cloud as a remote backend state, you should instead use the cloud block to configure its usage.

You can still use the backend remote for Terraform Cloud, but it's recommended to use the cloud backend block.

### terraform_remote _state
terraform_remote _state data source `retrieves the root module output values from another Terraform configuration`, using the latest state snapshot from the remote backend.

- from different folder
```
data "aws_subnet_ids" "subnet_ids" {
    vpc_id = data.vpc.main.id
    depends_on = [
        "data.aws_vpc.main"
    ]
}
```
