# Terraform Language

## Terraform files
- contain the configuration information about providers and resources.
- Terraform files are written in the Terraform Language and is the extension of `HCL​: HashiCorp Configuration Language`
- Terraform also supports an alternative syntax that is JSON-compatible​ (`.tf.json`)
- Blocks: containers for other content, represent an object
- - block types: can have zero or more labels and a body​
- - block label: name of a block
- Arguments: assign a value to a name​. They appear within blocks​
- Expressions: represnet a value, either literally or by referencing and combining other values
The special terraform configuration block type eg. terraform { … } is used to configure some behaviors of Terraform itself​
- In Terraform settings we can specify:​
- - required_version​ - The expected version of terraform​
- - required_providers​ - The providers that will be pulled during a terraform init​
​- - experiments​​ - Experimental language features, that the community can try and provide feedback​
​- - provider_meta​​ - module-specific information for provid

    ```
                terraform {
                    backend "s3" {
                        bucket = "terraform-state-dev-samboo"
                        key    = "dev/terraform-exampro.tfstate"
                        region = "us-east-1"
                    }
                    required_providers {
                        aws = {
                        source  = "hashicorp/aws"
                        version = "6.0.0-beta2"
                        }
                    }
                }
    ```

- 