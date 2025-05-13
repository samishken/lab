# LoadBalancers
- Cloud Controller
- what service is inside Kubernetes Cluster?
- How services interacts with the infrastructure?
- How services interact with Load Balancers in general?
- How the AWS Load Balancer Controller can create and manage Load Balancers that connect to services inside a Kubernetes cluster?

### LoadBalancer
- Load Balancer controller: helps use get loadbalancers (ALB, NLB)
- Node
- Global LoadBalancer: lives outside of regions.  
- 

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
