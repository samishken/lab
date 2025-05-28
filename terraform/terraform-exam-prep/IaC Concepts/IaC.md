# IaC

### Benefits of IaC
- Less human errors for misconfiguration
- Can easily manage expected state
- Can easily be shared among team members
- We write a configuration script to `automate` => `creating, updating or destroying` cloud infrastructure.
- IaC allows us to easily `share, version or inventory` our cloud infrastructure.

### Declarative+
- Terraform is declarative but the Terraform Language features imperative-like functionality.

### Declarative
- YAML, JSON, XML
- Limited or no support for imperative-like features.
- In some cases, you can add behaviour by extending the base language. E.g. CloudFormation Macros.

### Declarative|Imperative

- HCL-ish (Terraform Language)
-Supports: Loops (For Each), Dynamic Blocks, Locals, Complex Data Structure (Maps, Collections)

### Imperative
- Ruby, Python, JavaScript: Imperative features are the utility of the entire feature set of the programming language.

### Infrastructure Lifecycle
- How does IaC enhance the Infrastructure Lifecycle?

### Reliability
- IaC makes changes `idempotent`, consistent, repeatable, and predictable.

##### Idempotent
- No matter how many times you run IaC, you will always end up with the same state that is expected

### Manageability
- enable mutation via code
- revised, with minimal changes

### Sensibility
- avoid financial and reputational losses to even loss of life when considering government and military dependencies on infrastructure

### Provisioning vs Deployment vs Orchestration​

#### ​Provisioning​
- To prepare a server with systems, data, and software, and make it ready for network operation.​
- Using Configuration Management tools like Puppet, Ansible, Chef, Bash scripts, PowerShell, or Cloud-Init you can provision a server.​
- ​When you launch a cloud service and configure it you are “provisioning”​​

#### ​Deployment​​
- Deployment is the act of delivering a version of your application to run a provisioned server.​
- Deployment could be performed via AWS CodePipline, Harness, Jenkins, Github Actions, CircleCI​

#### ​Orchestration​​
- Orchestration is the act of coordinating multiple systems or services.​
- Orchestration is a common term when working with microservices, Containers, and Kubernetes.​
- Orchestration could be Kubernetes, Salt, Fabric​

### Configuration Drift​
- Configuration Drift is when provisioned infrastructure has an unexpected configuration change due to:​
- team members manually adjusting configuration options​
- malicious actors​
- side effects from APIs, SDK, or CLIs.​
eg. a junior developer turns on Delete on Termination for the production database.​

Configuration Drift going unnoticed could be a loss or breach of cloud services and residing data or result in interruption of services or unexpected downtime.​

#### How to detect configuration drift?​
- A compliance tool that can detect misconfiguration eg. AWS Config, Azure Policies, *GCP Security Health Analytics​"
- Built-in support for drift detection eg. `AWS CloudFormation Drift Detection​`
- Storing the expected state eg. `Terraform state files​`

#### How to correct configuration drift?​
- A compliance tool that can remediate (correct) misconfiguration e.g. AWS Config​
- Terraform `refresh` and `plan` commands​
- Manually correcting the configuration (not recommended)​
- Tearing down and setting up the infrastructure again​

Note: `Terraform refresh` command is not recommended

Please use the alias command: terraform apply -refresh-only -auto-approve or terraform apply -refresh-only

https://www.terraform.io/cli/commands/refresh#usage

#### How to prevent configuration drift?​
- `Immutable infrastructure`, always create and destroy, never reuse, Blue-Green deployment strategy.​
- - Servers are never modified after they are deployed​
- - Baking AMI images or containers via AWS Image Builder or HashiCorp Packer, or a build server eg. GCP Cloud Run​
- Using GitOps to version control our IaC, and peer review every single via Pull Requests change to infrastructure​

## What is GitOps?​
- GitOps is when you take Infrastructure as Code (IaC) and you use a git repository to introduce a formal process to review and accept changes to infrastructure code, once that code is accepted, it automatically triggers a deploy​