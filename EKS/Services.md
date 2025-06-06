# Kubernetes services

# cluster Ip
- Only allows service to service (port to port) communication within a cluster.

# NodePort
- Only allows service to service (port to port) communication within a vpc.

# LoadBalancer
- used to communicate with pods from internet.
- Loadbalancer we create on K8s using LoadBalancer service type isn't Declarative because it's created by AWS.
- 

# Ingress
- A single ingress resource can be used for microservices by defining host and path
- incoming traffic: define routing rule
- Use K8s kind called "ingress" to define Routing rules
        ```
            apiVersion: networking.k8s.io/v1
            kind: Ingress
            metadata:
            name: frontend-proxy
            annotations:
                alb.ingress.kubernetes.io/scheme: internet-facing
                alb.ingress.kubernetes.io/target-type: ip
            spec:
            ingressClassName: alb
            rules:
                - host: samboo.example.com
                http:
                    paths:
                    - path: "/"
                        pathType: Prefix
                        backend:
                        service:
                            name: opentelemetry-demo-frontendproxy
                            port:
                            number: 8080

        ```

## Kubernetes: LoadBalancer Service Type vs Ingress

In Kubernetes, both `LoadBalancer service` type and `Ingress` are used to expose services to external traffic. 
However, they serve different purposes and have distinct characteristics. 

## LoadBalancer Service Type

### Overview
- The LoadBalancer service type is a way to expose a service to external traffic by provisioning an external load balancer.
- It is typically used to expose a single service to the internet.

### Characteristics
- **Automatic Provisioning**: When a LoadBalancer service is created, Kubernetes automatically provisions an external load balancer from the cloud provider.
- **Single Service Exposure**: Each LoadBalancer service exposes a single service.
- **Cloud Provider Dependent**: The implementation and features of the LoadBalancer depend on the cloud provider (e.g., AWS, GCP, Azure).
- **Static IP**: It usually provides a static IP address for the service.

### Use Cases
- Suitable for exposing a single service to the internet.
- Ideal for simple use cases where advanced routing is not required.

## Ingress

### Overview
- Ingress is a Kubernetes resource that manages external access to services within a cluster, typically HTTP and HTTPS.
- It provides more advanced routing capabilities compared to the LoadBalancer service type.

### Characteristics
- **Advanced Routing**: Ingress can route traffic to multiple services based on hostnames, paths, and other rules.
- **Single Entry Point**: It provides a single entry point for multiple services.
- **TLS Termination**: Ingress can handle TLS termination, providing secure HTTPS access.
- **Requires Ingress Controller**: An Ingress resource requires an Ingress controller to be deployed in the cluster (e.g., NGINX, Traefik).

### Use Cases
- Suitable for exposing multiple services through a single IP address.
- Ideal for complex routing scenarios, such as path-based or host-based routing.
- Useful for managing SSL/TLS certificates and providing secure access.

## Comparison Table

| Feature                  | LoadBalancer Service Type | Ingress                        |
|--------------------------|---------------------------|-------------------------------|
| Provisioning             | Automatic by cloud provider| Requires Ingress controller   |
| Service Exposure         | Single service            | Multiple services             |
| Routing Capabilities     | Basic                     | Advanced (host/path-based)    |
| TLS Termination          | No                        | Yes                           |
| Cloud Provider Dependency| Yes                       | No                            |
| Use Case                 | Simple, single service    | Complex, multiple services    |

## Conclusion

Both LoadBalancer service type and Ingress are essential tools in Kubernetes for exposing services to external traffic. The choice between them depends on the specific requirements of your application. Use LoadBalancer for simple, single-service exposure and Ingress for more complex scenarios requiring advanced routing and secure access.
