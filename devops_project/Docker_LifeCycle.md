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