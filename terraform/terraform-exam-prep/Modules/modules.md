# Terraform Modules
- can be found publicly. Only verified & official modules can be found in search
- Public Module: terraform registry. Terraform registyr is integrated `directly into` Terraform
- `terraform init` command will `download and cache any modules`
    ```
            module "consul" {
                source = "hashicorp/consul/aws"
                version = "0.1.0"
            }
    ```
- Private Module: terraform cloud/enterprise
- Private registry modules have source strings of the form.
- need to do `terraform login`
    ```
            module "vpc" {
                source = "app.terraform.io/example_corp/vpc/aws"
                version = "0.9.2"
            }
    ```

## Standard Module Structure
### Root Module.
- The primary entry point is the Root Module.
- These are required files in the root directory.
- - - - `main.tf` - the entry point file of your module
- - - - `variables.tf` – variable that can be passed in
- - - - `Outputs.tf` – Outputed values
- - - - `README` – Describes how the module works
- - - - `LICENSE` – The license under which this module is available

---
### Nested Module
- `Nested modules` that are optional must be contained in the modules/ directory:

- - - - A submodule that contains a README is considered usable by external users
- - - - A submodule that does not contain a README is considered internal use only
- - - - Avoid using relative paths when sourcing module blocks.


## Example Standard Module Structure for Multiple Environments

```
my-terraform-module/
├── main.tf
├── variables.tf
├── outputs.tf
├── README.md
├── LICENSE
├── modules/
│   ├── network/
│   │   ├── main.tf
│   │   └── README.md
│   └── compute/
│       ├── main.tf
│       └── README.md
└── envs/
    ├── dev/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    ├── stage/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    ├── preprod/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    └── prod/
        ├── main.tf
        ├── variables.tf
        └── backend.tf
```

- **main.tf, variables.tf, outputs.tf**: Core module logic and definitions.
- **modules/**: Shared nested modules (e.g., network, compute).
- **envs/**: Contains directories for each environment (`dev`, `test`, `stage`, `prod`).
    - Each environment has its own `main.tf`, `variables.tf`, and `backend.tf` for environment-specific configuration and backend settings.

> **Tip:** In each environment’s `main.tf`, you can call the root module using relative paths and override variables as needed for that environment.

## Summary
- **Root Module**: Contains core files (`main.tf`, `variables.tf`, `outputs.tf`, `README.md`, `LICENSE`) that define the main logic and documentation for the module.
- **modules/**: Contains reusable nested modules for AWS services, including:
  - `network/`
  - `compute/`
  - `lambda/`
  - `eks/`
  - `s3/`
  - `ec2/`
  Each submodule has its own `main.tf` and README.md.
- **envs/**: Contains separate directories for each environment (`dev`, `staging`, `preprod`, `prod`). Each environment has its own `main.tf`, `variables.tf`, and `backend.tf` for environment-specific configuration and backend settings.
- **Best Practice**: In each environment’s `main.tf`, you can call the root module and override variables as needed for that environment.

This structure helps organize Terraform code for managing AWS resources across multiple environments using modular and reusable components.

```
my-terraform-module/
├── main.tf
├── variables.tf
├── outputs.tf
├── README.md
├── LICENSE
├── modules/
│   ├── network/
│   │   ├── main.tf
│   │   └── README.md
│   ├── compute/
│   │   ├── main.tf
│   │   └── README.md
│   ├── lambda/
│   │   ├── main.tf
│   │   └── README.md
│   ├── eks/
│   │   ├── main.tf
│   │   └── README.md
│   ├── s3/
│   │   ├── main.tf
│   │   └── README.md
│   └── ec2/
│       ├── main.tf
│       └── README.md
└── envs/
    ├── dev/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    ├── staging/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    ├── preprod/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── backend.tf
    └── prod/
        ├── main.tf
        ├── variables.tf
        └── backend.tf
```

- **modules/**: Now includes nested modules for AWS services: `lambda`, `eks`, `s3`, and `ec2`, each with its own `main.tf` and `README.md`.
- **envs/**: Contains directories for each environment (`dev`, `staging`, `preprod`, `prod`).