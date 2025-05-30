# Providers

- Terraform relies on plugins called providers to interact with cloud providers, SaaS providers, and other APIs.

- Terraform configurations must declare which providers they require so that Terraform can install and use them. Additionally, some providers require configuration (like endpoint URLs or cloud regions) before they can be used.
- Providers are required for your Terraform Configuration file to work.​

## What Providers Do
Each provider adds a set of resource types and/or data sources that Terraform can manage.

Every resource type is implemented by a provider; without providers, Terraform can't manage any kind of infrastructure.

Most providers configure a specific infrastructure platform (either cloud or self-hosted). Providers can also offer local utilities for tasks like generating random numbers for unique resource names.

## Trraform Registry

- Terraform Registry is a website portal to browse, download or publish available Providers or Modules​ (https://registry.terraform.io​)

## Terraform Modules​
* A Terraform module is a group of configuration files that provide common configuration functionality.​
- - Enforces best practices​
- - Reduce the amount of code​
- - Reduce time to develop scripts​