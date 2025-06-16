# Kubernetes Requests and Limits
- Must be implemented if we want to create well behaved K8s cluster.

- we can't request more memory than the request.
- If we request more cpu than the limit.  Pod will be throttle.
---
### Resource Requests
- The real purpose of specifying `requests` is when we're deploying a pod to a cluster it will allow the cluster manager to ensure that there is enough memory on the node (server), to allow that pod to run comfortably.
- By setting request resources: we enable the cluster manager to make intelligent decisions about whether or not a node is able to run a pod or not.
- Resource request are either memory or cpu requests.
- memory requests
- cpu requests: 
- Resourses will be added inside the container specification

        
            apiVersion: apps/v1
            kind: Deployment
            metadata:
            name: queue
            spec:
                selector:
                    matchLabels:
                    app: queue
                replicas: 1
                template: # template for the pods
                    metadata:
                    labels:
                        app: queue
                    spec:
                    containers:
                    - name: queue
                        image: richardchesterwood/k8s-fleetman-queue:release2
                        resources:     ##  Adding memory and cpu requests inside container specification
                            requests:
                                memory: "64Mi"   #### 1Mi = 1024Ki => 1Ki = 1024bytes
                                cpu: "250m"  

- 

---
### Limits
- memory and cpu limits
- For a memory limit, if the actual memory used by your container when it's running exceeds the limit for any reason then the container will be killed.  if you set a limit and that limit is exceeded then your container will be killed.
- if the CPU is exceeded, then the container isn't killed, but the CPU will be, I'm calling it clamped here throttling.

        apiVersion: apps/v1
        kind: Deployment
        metadata:
        name: queue
        spec:
        selector:
            matchLabels:
            app: queue
        replicas: 1
        template: # template for the pods
            metadata:
            labels:
                app: queue
            spec:
            containers:
            - name: queue
                image: richardchesterwood/k8s-fleetman-queue:release2
                resources:
                requests:
                    memory: "64Mi"
                    cpu: "250m"
                limits:
                    memory: "128Mi"
                    cpu: "500m"
