# LoadBalancers
- Cloud Controller
- what service is inside Kubernetes Cluster?
- How services interacts with the infrastructure?
- How services interact with Load Balancers in general?
- How the AWS Load Balancer Controller can create and manage Load Balancers that connect to services inside a Kubernetes cluster?
- Kube-proxy directs network traffic to pods within a Kubernetes cluster by maintaining network rules on each node. It primarily uses iptables in its default mode to route traffic between services and pods. 
- Kube-proxy watches the Kubernetes API server for new services and updates its network rules accordingly, ensuring traffic is routed to the correct backend pods
- kube-proxy knows how to send the pods to the right pod.  It will take the traffic and route it to the right pod.


``` External users
    --> LOAD BALANCER 
            ------->   ____________________________  
                       |k8s cluster    
                       | -> Node-|
                       |    ----> pods - pods - pods
                       |___________________________
```


### LoadBalancer
- Load Balancer controller: helps use get loadbalancers (ALB, NLB)
- Cluster -> Node -> Pods -> kube-proxy
- Load balancer outside of the cluster
- load balancer inside of the cluster:  looks for Annotations  (ALB or NLB)
- Global LoadBalancer: lives outside of regions.  


### Gateway Ingress
- Ingress rules   opentelemetry-demo-frontend   opentelemetry-demo-frontendproxy
- Service mesh (Istio)
- AWS Lattice


- Best Practice
🔵 opentelemetry-demo-frontend
Purpose: This is the main user-facing frontend application.
Technology: Usually implemented in JavaScript/TypeScript using React. 
Function:
- Renders the user interface (UI) for the demo application.
- Handles interactions from users such as product views, checkout, etc.
- Makes HTTP requests to backend services (e.g., product catalog, cart, checkout).

🟢 opentelemetry-demo-frontendproxy
Purpose: Acts as a reverse proxy in front of the frontend and backend services.
Technology: Implemented in Go (Golang).
Function:
- Routes requests from the browser to the appropriate backend services.
- Can inject telemetry headers to propagate trace context.
- May help simulate more realistic service-to-service communication for trace generation.
- Adds an additional network hop for better observability demonstration.


### VPC Lattice  
