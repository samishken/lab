# EKS Networking

### AWS Networking
- pods inside cluster should be able to talk to one another
* VPC: network boundary for ourselves. Eni to connect with control plane.
* * -> Subnet: anthing inside the vpc gets ip address.
* * * -> Node: in the cluster.
* * * * -> ENI: attached to the node like an outlet.  IP address will be attached to it like a cable. 
* * * * * There are three types of ENIs. 
* * * * * * One for node so the node get IP address. Can have upto 10 IP addresses depending on the size.
* * * * * * Second one for vpc to connct dataplane with api server.  
* * * * * * thrid for pod inside node. Pod will have an ip address
* * * * * * * Pod: inside the node will have it's own ip address

<br>

---
### EKS CNI (VPC-CNI)
- Node ENI allocates ip addresses to pods.
- when the limit for on ENI reaches, VPC-CNI which is attached to the node will create a second one.  As more pods join the Node VPC-CNI will add ENIs until it reaches the limit.
- the size of the node (ec2 type) determines how many ENI's we can add
-
- The Amazon VPC CNI plugin for Kubernetes is the networking plugin for Pod networking in Amazon EKS clusters. The plugin is responsible for allocating VPC IP addresses to Kubernetes nodes and configuring the necessary networking for Pods on each node.
-
- "Prefix Deleegation": when set to true, 
- 
- "IPv6" - enabled from the start.
- 

### Default
- aws node (daemonset)
- 
- Coredns
- coredns: is used for service discovery inside cluster
- kube-proxy
- kube-proxy: route traffic


--- 
### Network Policy
- manage how network is managed between pod

