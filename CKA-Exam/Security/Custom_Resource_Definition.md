# Custom Resource Definition (CRD)
- Operator Framework:
- - combines Custom Resource and Custom controller

- when we create a `deployment` definition file, the DEFINITION CONTROLLER is responsible to use the information on the file and execute.
- CONTROLLER is built-in to the kubernetes and it's available. 
- CONTROLLER is a process that runs in the background and its job is to continously monitor the status of resources that it's supposed to manage the deployment that we created.
- when we create, update, delete the deployment, CONTROLLER makes the necessary changes on the cluster to match what we have done.

- ETCD stores all information.
- SCHEDULER is a core component that assigns pods to nodes in a Kubernetes cluster