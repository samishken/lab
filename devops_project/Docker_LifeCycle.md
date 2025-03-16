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
