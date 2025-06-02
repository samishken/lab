# Terraform Resources

Resources in configuration files represent `infrastructure objects` e.g. Virtual Machines, Databases, Virtual Network Components, Storage…..

A resource type determines the kind of infrastructure object:

e.g. `aws_instance` is an AWS EC2 instance

A resource belongs to a provider.

Some resource types provide a `special timeouts nested block` argument that allows you to customize how long certain operations are allowed to take before being considered to have failed.


### Complex Types
A complex type is a type that groups multiple values into a single value.

Complex types are represented by type constructors, but several of them also have shorthand keyword versions.

There are two categories of complex types:
- collection types (for grouping similar values): List, Map, Set
- structural types (for grouping potentially dissimilar values): Tuple, Object

### Collection Types
A collection type allows multiple values of one other type to be grouped together as a single value.

The type of value within a collection is called its element type. 

The three kinds of collection type `list, map, set`

`List` – It's like an array, you use an integer as the index to retrieve the value.  Example: ["mars", "earth", "moon"]

`Map` – It's like a ruby hash or single nested JSON object. You use a key as the index to retrieve the value

`Set` – Is similar to a list but has no secondary index or preserved ordering, all values must be of the same type and will be cast to match based on the first element

### Structural Types
A structural type allows multiple values of several distinct types to be grouped together as a single value.

Structural types require a `schema` as an argument, to specify which types are allowed for which elements.

The two kinds of structural type, `object`, and `tuple`

Object is a map with more explicit keying

- object({ name=string, age=number })

Tuple. Multiple return types with parameters

- tuple([string, number, bool])
