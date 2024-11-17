## vimrc - can help setup command line

# kubectl reference from k8s documentation
https://kubernetes.io/docs/reference/kubectl/generated/kubectl/

𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲 𝗘𝘅𝗽𝗹𝗮𝗶𝗻𝗲𝗱!

- Cluster: The overall Kubernetes environment, managing applications across nodes.
- Node: A machine (Master or Worker) in the cluster that runs workloads.
- Pod: The smallest deployable unit, containing one or more containers, running on a node.
- Service: Provides stable access to pods, with load balancing.
- Namespace: Logical partition to organize resources within the cluster.
- API Server: Handles requests to the cluster.
- etcd: Stores all cluster data.
- Scheduler: Assigns pods to nodes.
- Controller manager: 
- Kubelet: Manages pod lifecycle on each node.
- Kube Proxy: Manages network communication for services.


## Pod
-- A pod is the smallest element on a k8s cluster
-- Pods are ephemeral (short term). Shorter lifespan.
-- Pods are constantly changing and being moved around nodes.
--- "kubectl run nginx --image=nginx --dry-run=client"
--- To comunicate with the pod "k exec -it nginx -- /bin/bash"
--- 'htop' command helps us see the thing running inside pods
-------- contains information about storage and netwroking
-------- to get detailed information about a particulat pod "k get pod nginx -o yaml less"
-- A pod is a collection of containers & other resources
---- Single container
---- Multi container
---- Init container
---- Pod logs:  "kubectl logs nginx-phpfpm -c php-fpm-container"

## Networking
- # Pods
---- CNI plugin (container networking plugin) enables networking between pods
--------- CNI plugin Provides network connectivity to containers
--------- Configures network interfaces in containers
--------- Assigns IP addresses and sets up routes ----> IPTables on nodes
------------------ Cilium
------------------ Calico
------------------ Flannel (CNI pluging for rancher)
------------------ The Amazon VPC CNI plugin is the default CNI used by Amazon EKS.
---- Each pod gets its own IP address (-o wide)
---- By default, pods can connect to all pods on all nodes (need to create network policies)
---- Containers in pods can communicate with each other through localhost 

- # Services
---- A service offers a consistent address to access a set of pods. 
---- Services are essential because Pods are ephemeral (short term lifespan) and also moved around different nodes.
---- One IP address (endpoint) 
-    - # ClusterIP `is the default service. Creates cluster-wide IP for service`
-    - # NodePort `Exposes a port on each node allowing direct access to the service through any nodes' IP address`
-    - # LoadBalancer `Used for cloud providers. It will create LB to route traffice into the cluster`

- # Ingress
---- Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster.
---- Enables connection from outside the cluster. 
---- Example: www.google.com/frontend will allow connction to 'frontend' services
- # `Ingress is a collection of rules that allow inbound connections to reach the`
    `endpoints defined by a backend. An Ingress can be configured to give`
    `services externally-reachable urls, load balance traffic, terminate SSL,`
    `offer name based virtual hosting etc.`
-    - # Ingres Resources `configuration / definition files`
-    - # Ingres Controller `is a load balancer that connects Kubernetes services to external services and manages traffic routing within a Kubernetes cluste`
-----------  Istio
-----------  Nginx
-----------  Traefik
-----------  HAPROXY
-----------  Cilium
-----------  Cloudi AGIC (GCP https(s) LoadBalancer)

# Storage
---- Volumes store data
---- A pod can have multiple containers sharing one volume.
-    - # Ephemeral Storage `short term`
-    - # Persistent Storage


# kustomize
- Can help manuplate with how much resource we want to deploy to each environment


# Sosivio - resource optimization
- cost savings