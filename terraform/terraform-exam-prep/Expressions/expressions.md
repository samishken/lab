# Introduction to Terraform Expressions
- Expressions are used to refer to or compute values within a configuration. 
- Terraform Expressions: 
- `Types and Values`: The result of an expression is a value. All values have a type
- - - - primitive types
- - - - string:  "hello"
- - - - number: 233
- - - - bool: true/false
- - - - no type: 
- - - - null : null represents absence or omission, when you want to use the underlying default of a provider’s resource configuration option
- `Strings and Templates`
- `References to Values`
- `Operators`: mathematical operations
- - - - "a*b", "a == b", a <= b, 
- - - - "a / b"
- - - - "a  % b"
- - - - OR "a || b"
- `Function Calls`
- `Conditional Expressions`: var.a != "" ? var.a : "default-a"
- `For Expressions`
- `Splat Expressions`
- `Dynamic Blocks`:  allows you dynamically construct repeatable nested blocks
- - - - Let's say you need to create a bunch of ingress rules for an EC2 Security Group.
- - - - Define objects in locals:
- - - - Set dynamic block and utilized `for_each` bloack
- `Type Constraints`
- `Version Constraints`: Terraform utilizes Semantic Versioning for specifying Terraform, Providers, and Modules versions
- - - - `MAJOR` version when you make incompatible API changes,
- - - - `MINOR` version when you add functionality in a backwards-compatible manner, and
- - - - `PATCH` version when you make backwards-compatible bug fixes. Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

= `terraform console`
=> "Hello %{if var.hello == "barsoon"}Mars&{else}World%{endif}"


## - `For Expressions`
- `[for s in var.list : upper(s)]`

worlds=["barsoon", "jasoom", "sasoom", "cosoom"]
{for i,w in var.worlds : "${i}" => upper(w)}

worlds_map={
    "barsoon": "mars",
    "jasoom": "earth",
    "sasoom": "jupiter",
    "cosoom": "venus"
}
- `[for k,v in var.map : length(k) + length(v)]`
- `[for i,v in var.list : "${i} is ${v}"]`


## Splat Operations
## — Splat Expressions
- A splat expression provides a shorter expression for 'for' expressions

`What is a splat operator?`
- A splat operator is represented by an asterisk (*), it originates from the ruby language
- Splats in Terraform are used to rollup or soak up a bunch of iterations in a for expression
- `For lists, sets, and tuples`
- Can be written list this: Splat expressions have a special behavior when you apply them to lists
- - - - If the value is anything other than a null value then the splat expression will transform it into a single-element list
- - - - If the value is null then the splat expression will return an empty tuple.
This behavior is useful for modules that accept optional input variables whose default value is null to represent the absence of any value to adapt the variable value to work with other Terraform language features that are designed to work with collections.


## A version constraint is a string containing one or more conditions, separated by commas.

- `=` or no operator. Match exact version number e.g. “1.0.0”, “=1.0.0”
- `!=` Excludes an exact version number e.g. “!=1.0.0”
- `> >= < <=` Compare against a specific version e.g. “>= 1.0.0”
- `~>` Allow only the rightmost version (last number) to increment e.g. ~> 1.0.0”

## Progressive Versioning
Progressive Versioning is the practice of using the latest version to keep a proactive stance of security, modernity, and development agility

Practicing Good Hygiene

By being up to date you are pushing left things you will need to fix to stay compatible. You will have to deal with smaller problems instead of dealing with a big problem later on

Run Nightly Builds of your golden images or terraform plan as a warning signal to budget the time to improve for outage.

A nightly build is an automated workflow that occurs at night when developers are asleep. If the build breaks because a change is required for the code, the developers will see this upon arrival in the morning and be able to budget accordingly.