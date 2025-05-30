# Variables and 

## Variables
- Variables are defined via variable blocks.
- Variable blocks include: Default, type, Description, Validation, Sensitive
- Variable types:
- - 
- - 

#### Variable Definitions Files
- A variable definitions file allows you to set the values for multiple variables at once.
- By default `terraform.tfvars` will be autoloaded when included in the root of your project directory

#### Variables via Environment Variables
- A variable value can be defined by Environment Variables
- Variable starting with `TF_ VAR _` name will be read and loaded
- Example: global variable for Image ID `export TF_VAR_image_id=ami-abc123`
- 

## Outputs
- Output Values are computed values after a Terraform apply is performed. Outputs allow you:
- - - to obtain information after resource provisioning e.g. public IP address
- - - output a file of values for programmatic integration
- - - Cross-reference stacks via outputs in a state file via terraform_remote _state
- You can optionally provide a description
- You can mark the output as sensitive so it does not show in the output of your Terminal
- Sensitive outputs will still be visible within the state file.
- To print all the outputs for a state file use the terraform output
- Print a specific output with terraform output name
- Use the –json flag to get output as json data.
- Use the –raw flag to preserve quotes for 
- `terraform output`
- `terraform output -json`
- `terraform output lb_url`
- `terraform output -json | jq -r ".public_ip.value"`

                    ```
                    output "db_password {
                        value = 
                        sensitive = false
                        description = "out put of public ip"
                    }
                    ```


## Local values
- A local value (locals) assigns a name to an expression, so you can use it multiple times within a module without repeating it.
- Locals are set using the locals block ← Static value
- You can define `multiple` locals blocks ← computed values
- You can `reference locals within locals`
- Once a local value is declared, you can reference it in expressions as `local.NAME`.
- When you are referencing `you use the singular “local”`
- Locals help can help DRY up your code.

It is best practice to use locals sparingly since Terraform is intended to be declarative and overuse of locals can make it difficult to determine what the code is doing.

## Data Sources ***
- Data sources allow Terraform to `use information defined outside of Terraform`, defined by another separate Terraform configuration, or modified by functions.
- You specify what kind of external resource you want to select
- You use filters to narrow down the selection
- You use data. to reference data sources


## References to Named Values
Named Values are `built-in expressions` to `reference various values` such as:

Resources Resource Type.Name e.g. aws_instance.my _server
* Input variables var.Name
* Local values local.Name
* Child module outputs module.Name
* Data sources data.Data Type.Name
* Filesystem and workspace info

- path.module - path of the module where the expression is placed
- path.root - path of the root module of the configuration
- path.cwd - path of the current working directory
- terraform.workspace – name of the currently selected workspace
Block-local values (within the body of blocks)

* count.index (when you use the count meta argument)
* each.key / each.value (when you use the for_each meta argument )
* self. - self reference information within the block (provisioners and connections)

Named values resemble the attribute notation for map (object) values but are not objects and do not act as objects.

You `cannot use square brackets` to access attributes of Named Values like an object.
