# Terraform Basics

## Terraform Lifecycle
- Code tf file -> Terraform Init -> Terraform Plan -> terraform Validate -> Terraform Apply
---
## Change management & automation & ChangeSet
### What is Change Management?​
- A standard approach to apply change, and resolving conflicts brought about by change.​
- In the context of Infrastructure as Code (IaC), Change management is the procedure that will be followed when resources are modified and applied via configuration script.

### What is Change Automation?​
- A way of automatically creating a consistent, systematic, and predictable way of managing change requests via controls and policies​
- Terraform uses Change Automation in the form of Execution Plans and Resources graphs to apply and review complex changesets​

### What is a ChangeSet?​
- A collection of commits that represent changes made to a versioning repository. 
- IaC uses ChangeSets so you can see what has changed by who over-time.​
- Change Automation allows you to know exactly what Terraform will change and in what order, avoiding many possible human errors.​
---
## Execution Plans
- An Execution Plan is a manual review of what will `add, change or destroy` before you apply changes eg. terraform apply​
## Visualizing Execution Plans​
- You can `visualize an execution` plan as a graph using the `terraform graph` command​.  `terraform graph | dot -Tsvg > graph.svg`
- Terraform will output a GraphViz file (you’ll need GraphViz installed to view the file)​
## Resource Graph
- Terraform builds a dependency graph from the Terraform configurations, and walks this graph to generate plans, refresh state, and more. ​

---
##Terraform Core and Terraform Plugins​
Terraform is logically split into two main parts: ​

### Terraform Core​
- uses remote procedure calls (RPC) to communicate with Terraform Plugins​

### Terraform Plugins​
- expose an implementation for a specific service, or provisioner​
---

## Terraform Up and Running


