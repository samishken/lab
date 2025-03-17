# Design a Kubernetes Cluster

# Production level clusters

# High Availability in Kubernetes
- what happens when we lost the controlplane cluster?
- - pods on worker nodes work until they fail
- - high availability control plane is needed.
- - - - 
- How to create HA for control plane?
- - two control plane with load balancer
- - Controller and Scheduler: how to avoid duplication?
- - - - create Active/Passive `kube-controller-manager --leader-elect true [other options]`
- - - - ETCD: 