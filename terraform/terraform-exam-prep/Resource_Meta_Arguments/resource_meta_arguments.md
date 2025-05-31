# Resource Meta Arguments
- Terraform language defines several meta-arguments, which can be used with any `resource type to change the behavior of resources`.

-  - `depends_on`, for specifying explicit dependencies. `depends_on` allows you to explicitly specify a dependency of a resource.
-  - `count`, for creating multiple resource instances according to a count.  When you are managing a pool of objects eg. a fleet of Virtual Machines you can use `count`.
-  - `for_each`, to create multiple instances according to a map, or set of strings. you can iterate over a map for more dynamic values.
- - - - each.key – print out the current key
- - - - each.value – print out the current value
-  - `provider`, for selecting a non-default provider configuration
-  - `lifecycle`, for lifecycle customizations
-  - `provisioner` and connection, for taking extra actions after resource creation


## When to Use count
Use count when:
- All resources are identical or vary by index.
- You want to control the number of resources with a number.

## When to Use for_each
Use for_each when:
- Each resource is uniquely named or configured.
- You're working with a map or set and need to preserve identity.


## Resource Behaviour
When you execute an execution order via `Terraform Apply` it will perform one of the following to a resource:

- `Create`: resources that exist in the configuration but are not associated with a real infrastructure object in the state.
- `Destroy`: resources that exist in the state but no longer exist in the configuration.
- `Update in-place`: resources whose arguments have changed.
- `Destroy and re-create`: resources whose arguments have changed but which cannot be updated in-place due to remote API limitations.

## Lifecycle
`Lifecycle` block allows you to change what happens to resources e.g. create, update, destroy.

Lifecycle blocks are nested within resources

`create_before _destroy` (bool): When replacing a resource first create the new resource before deleting it (the default is destroy old first)

`prevent_destroy` (bool) - Ensures a resource is not destroyed

`ignore_changes` (list of attributes): Don’t change the resource (create, update, destroy) if a change occurs for the listed attributes.

```
  lifecycle {
    prevent_destroy = true
    ignore_changes = [
      tags["Environment"],
      user_data,
    ]
    create_before_destroy = true
  }
```

## Alias
- If you need to override the default provider for a resource you can create an alternative provider with `alias`
- You reference the alias under the attribute provider for a resource.

            ```
            provider "aws" {
            region = "us-east-1"
            }

            provider "google" {
            alias = "west"
            region  = "us-west-1"
            }
            ```
`
- `alias` is used to create multiple configurations of the same provider. This is useful when you want to:
- - - - Use the same provider with different settings (e.g., regions, accounts, credentials)
- - - - Manage multiple cloud environments (e.g., deploy resources in two different AWS regions or GCP projects)
- - - - Avoid provider conflicts in modules