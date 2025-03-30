# Design a Kubernetes Cluster

# Production level clusters

# High Availability in Kubernetes
- what happens when we lose the controlplane cluster?
- - pods on worker nodes work until they fail
- - high availability control plane is needed.
- - - - 
- How to create HA for control plane?
#### Tow master nodes for HA
- - API Server: how's the API Server works in this case?
- - - - two control plane nodes with load balancer like Nginx
- - - - this will help us send kubectl request to just one of API Servers

- - Controller and Scheduler: how to avoid duplication?
- - - - create Active/Passive `kube-controller-manager --leader-elect true [other options]`
- - ETCD: there are two way to setup ETCD
- - - - First: setting up ETCD on master node.  This is risky because if one node goes down both an ETCD member and control plane instance is lost and reduncancy is compromised.
- - - - Second: Setting up ETCD with external server.  Harder to setup and needs a lot of servers.
