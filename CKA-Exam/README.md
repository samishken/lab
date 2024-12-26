#


### Kubernetes Architecture
##### Control Plane
The master node manages the Kubernetes cluster and is responsible for the orchestration of worker nodes. It contains the following components:
    • API Server (kube-apiserver)
        ○ The main entry point to the Kubernetes control plane.
        ○ Exposes RESTful APIs for communication with the cluster.
        ○ Handles authentication, authorization, and validation of requests.
    • Controller Manager (kube-controller-manager)
        ○ Runs controller processes that ensure the desired state of the cluster.
        ○ Key controllers include:
            § Node Controller: Manages node availability and health.
            § Replication Controller: Ensures the correct number of pod replicas.
            § Endpoint Controller: Updates endpoints for services.
            § Job Controller: Manages job objects.
    • Scheduler (kube-scheduler)
        ○ Assigns pods to nodes based on resource availability, constraints, and policies.
        ○ Considers CPU, memory, affinity rules, and taints/tolerations.
    • etcd
        ○ A distributed key-value store that acts as the cluster's backing store.
        ○ Stores all cluster data, including configuration, secrets, and the current state.

##### Data Plane
Worker nodes host the application workloads (pods) and provide the runtime environment for containers. Each worker node includes:
    • Kubelet
        ○ An agent that communicates with the API server to ensure containers are running as specified.
        ○ Manages pod lifecycle on the node.
    • Kube-proxy
        ○ A network proxy that maintains network rules for pod communication.
        ○ Implements service discovery and routing between pods and services.
    • Container Runtime
        ○ Runs and manages containers on the node (e.g., Docker, containerd, CRI-O).
Ensures containers are pulled, started, and stopped as needed.
