# Storage for EKS Cluster

### PVC: persistent volume claim

### EBS Volume (elastic bloack storage)
- Node 


### StatefulSet
- Creates N number of replicas for pods and persistent volumes.
- Each pod will have it's own ppersistent volume and persistent volumes claim storage. Each pod will have it's own storage.
- if the pod goes away, the volume, the data will remain until another pod is recreated.

### Deployment
- Creates N number of replicas, scales using HPA.
- In deployment case all pods share the same persistent volume using the same persistent volume claim.
- All pods share the same storage.

### Daemonset
- Deploys one or multiple pods in each node of the cluster.  Example poos that we want to deplploy on all nodes will be the ones that collect logs, metrics, and configure network policies.

