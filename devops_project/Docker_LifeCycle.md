# Docker LifeCycle
- Docker containers go through five main stages: Created, Running, Paused, Stopped, and Deleted. 
- FIRST: Setup Dockerfile:
- SECOND: Create docker image
- THIRD: Create and run docker container

# kubernetes
- Run this after deploying k8s cluster: `aws eks update-kubeconfig --region REGION-NAME --name CLUSTER-NAME`

# Docker compose
- 

# Docker vs Kubernetes
- Docker works to solve "it works on my machine" issue
- containers are ephemeral ( short lived)
- 
- Kubernetes

# Docker Compose vs Kubernetes


# kubernetes Service Account
- user account vs Service account
- Roles -> Rolebinding -> Service account
- How do we connect one service with another?
- - - - If Microservice_A needs to connect to Microservice_B, in the environment of Microservice_A POD, we add Service name of Microservice_B
- - - - We can also use ConfigMaps to connect two microservices.

# kubernetes deployment
- Deployment resource provides high availablity
- Scaling & healing 
- - - - Replicas
- - - - Vertical scaling: add more power to resources (more memory, more cpu)
- - - - Horizontal scaling: increase loads (multiple instances)
- - - - Probes: 
- - - - Readiness probes: verifies if container is ready to receive traffic
- - - - Liviness probes: checks health of container (determins if container is still running & functioning well)



# kubernetes service
- Service resource
- Service discovery

# Ingress
- why use Ingress than ALB (using Service type Loadbalancer disadvantages)
- 1) It's not declarative
- 2) Cost: if we have more than 1 microservice that need outside access, then we need a lot of LBs which is expensive.
- 3) We will be tied to ALB only. We won't have the flexibility to use other loadbalancers like nginx, F5, Traffik
- 4) Loadbalancer only works on public cloud service

 ##### ingress advantages
 - 1) Declarative.  we can use yaml file to create it.
 - 2) cost effective. One LBs with host or route based routing is enough for multiple microservices
 - 3) Flexible: flexible to use multiple load balancer tools. can be used on Minikube
 - 4) Not CCM dependent: not dependent on public cloud services (aws, gcp, azure)


-- When we change the service type ClusterIp to load balancer, kube API Server instructs the cloud control manager, which creates a load balancer within the VPC. The load balancer can talk to the front end using the private subnet.
-- Right at the same time, the load balancer is also connected to the public subnet so that people from external world can talk to the load balancer using load balancer DNS name and their request is sent to the front end. 
-- When we create a service of type load balancer, CCM reads that information and it creates the load balancer. We access this front end service on a random domain name which is created by CCM (Example: a77fasldfjfadslfldfj-27429697.us-west-2.elb.amazonaws.com (A Record)). 

 -- Ingress: Kubernetes has a resource of `kind: ingress`, INGRESS can help us with defining the routing rules for our incoming traffic to the cluster. Routing rule can only be defined if we use Ingress resource.
 -- Ingress controller: when you create a Kubernetes resource of type ingress, nothing happens.  Only when this ingress is read by the ingress controller which is a Kubernetes controller. Ingress controller reads that YAML file understands what is the exact requirement and it creates load balancer accordingly.
 -- if we keep the service type as ClusterIP or NodePort, and if we use Ingress resource using yaml for a microservice, Ingress controller reads that YAML file and according to the rules defined in the ingress file, it creates the load balancer.

 