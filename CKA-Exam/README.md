# Kubernetes

## Kubernetes Architecture
<br><br>

## Control Plane
The master node manages the Kubernetes cluster and is responsible for the orchestration of worker nodes. It contains the following components:
####  API Server (kube-apiserver)
        - The main entry point to the Kubernetes control plane. <br>
        - Authenticate User, Validate Request, Retrieve data, Update ETCD, Scheduler, Kubelet <br>
        - Exposes RESTful APIs for communication with the cluster. <br>
        - Handles authentication, authorization, and validation of requests. <br>
#### Controller Manager (kube-controller-manager)  
        - Runs controller processes that ensure the desired state of the cluster. <br>
        - monitors, continously on the look out for the state of pods.
        - Checks every 5 seconds. Gives 40 seconds for bad Pods to come back up. 
        - Key controllers include: <br>
            ---- Node Controller: Manages node availability and health. <br>
            ---- Replication Controller: Ensures the correct number of pod replicas. <br>
            ---- Endpoint Controller: Updates endpoints for services. <br>
            ---- Job Controller: Manages job objects. <br>
#### Scheduler (kube-scheduler)  
        - Assigns pods to nodes based on resource availability, constraints, and policies. <br>
        - Considers CPU, memory, affinity rules, and taints/tolerations. <br>
        - Decides which pod goes to which node <br>
        - ps -aux | grep scheduler <br>
#### etcd  
        - A distributed key-value store that acts as the cluster's backing store. <br>
        - Stores all cluster data, including configuration, secrets, and the current state. <br>
        - Nodes, PODs, Configs, Secrets, Accounts, Roles, Bindings, Others. <br>
        - ./etcdctl version <br>
        - ./etcdctl get key1
        - ./etcdctl put key1 value1

## Data Plane
Worker nodes host the application workloads (pods) and provide the runtime environment for containers. Each worker node includes:
####     Kubelet <br>
        - An agent that communicates with the API server to ensure containers are running as specified. <br>
        - Manages pod lifecycle on the node. <br>
        - ps -aux | grep kubelet <br>
####     Kube-proxy <br>
        - A network proxy that maintains network rules for pod communication. <br>
        - Implements service discovery and routing between pods and services. <br>
####    Container Runtime <br>
        - Runs and manages containers on the node (e.g., Docker, containerd, CRI-O). <br>
        - Ensures containers are pulled, started, and stopped as needed. <br>


## Networking
##### Default Service kube-dns
- Kubernetes creates DNS records for Services and Pods. You can contact Services with consistent DNS names instead of IP addresses.
- For Pod (webapp) to connect to Pod (database), first it looks for the IP address of DB Pod inside Kube-dns records. Once confirmed then it goes ahead and make the connection.

## Docker vs ContainerD
        - 

#### Pod
- A Pod is a single instance of an application. A Pod is the smallest object that we can create in Kubernetes.
- Pods are ephemeral in Kubernetes, meaning they are intended to be disposable and replaceable
- A pod can be multi-container (we can add helper containers). Example, Service mesh and Sidecar
- Connect to pod `kubectl exec -it POD-NAME -- sh`
- `kubectl run nginx --image=nginx`
- `kubectl run redis --image=redis --dry-run -o yaml > redis-pod.yml`
- `kubectl logs POD-NAME`


#### ReplicaSets
- purpose is to maintain a stable set of replica Pods running at any given time.
- `kubectl scale rs new-replica-set --replicas=5`  [update replicas number]


#### Deployments
- A Deployment manages a set of Pods to run an application workload, usually one that doesn't maintain state.
- tells Kubernetes how to create or modify instances of the pods that hold a containerized application. 
- `kubectl get all`
- `kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml`

#### Services
- Node Port - Exposes the Service on each Node's IP at a static port (the NodePort).
- ClusterIP - Exposes the Service on a cluster-internal IP
- LoadBalancer - Exposes the Service externally using an external load balancer. Kubernetes does not directly offer a load balancing component; you must provide one, or you can integrate your Kubernetes cluster with a cloud provider.
<br>
- Use lables and selectors to connect Services with Pods


#### Namespaces
- namespaces provide a mechanism for isolating groups of resources within a single cluster
- partitioning resources
- kube-system
- Default namespace
- kube-public


#### Imperative vs Declarative
- Imperative: a set of instruction added step by step
----- `kubectl run --image=nginx nginx`
----- `kubectl create deployment --image=nginx nginx`
----- ```kubectl create deployment --image=nginx nginx --dry-run=client -o yaml```
----- `kubectl replace -f nginx.yml`
----- `kubectl expose deployment nginx --port 80`
----- `kubectl edit deployment nginx`
----- `kubectl scale deploymenbt nginx --replicas=5`

- Declarative: declare the final outcome (Terraform, Ansible, Groovy)
----- add declarative files


<br>

<br>
# Kubernetes Architecture Icons

A K8s and Cloud-Native icon set for building cloud-native architecture diagrams


<img src="examples/k8s-splash-example.svg" width="100%" />

# Included Tools

- How to use the [SVG-to-PNG Conversion tool](docs/tools/svg-to-png.md) (supports any custom size)
- How to use the [Package Release tool](docs/tools/package-release.md) to aid in publishing new releases

# Included Files

- How to use the original [Illustrator file](docs/files/k8-architecture-icons.md) for mass svg export or to add your own icon.

# Icon Directory

## Cluster and Node Management

<table>
  <tr>
    <td><img src="icons/svg/cluster.svg" width="50px;" alt=""/></td>
    <td><a href="docs/cluster.md">Cluster</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/controller-manager.svg" width="50px;" alt=""/></td>
    <td><a href="docs/controller-manager.md">Controller Manager</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/cloud-controller-manager.svg" width="50px;" alt=""/></td>
    <td><a href="docs/cloud-controller-manager.md">Cloud Controller Manager</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/control-plane-node.svg" width="50px;" alt=""/></td>
    <td><a href="docs/control-plane-node.md">Control Plane Node</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/worker-node.svg" width="50px;" alt=""/></td>
    <td><a href="docs/worker-node.md">Worker Node</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/custom-resource-definition.svg" width="50px;" alt=""/></td>
    <td><a href="docs/custom-resource-definition.md">Custom Resource Defintion</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/namespace.svg" width="50px;" alt=""/></td>
    <td><a href="docs/namespace.md">Namespace</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/scheduler.svg" width="50px;" alt=""/></td>
    <td><a href="docs/scheduler.md">Scheduler</a></td>
  </tr>
</table>

## API

<table>
  <tr>
    <td><img src="icons/svg/api-server.svg" width="50px;" alt=""/></td>
    <td><a href="docs/api-server.md">API Server</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/kube-ctl.svg" width="50px;" alt=""/></td>
    <td><a href="docs/kube-ctl.md">Kube CTL</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/generic-manifest-file.svg" width="50px;" alt=""/></td>
    <td><a href="docs/generic-manifest-file.md">Generic Mainfest File</a></td>
  </tr>
</table>

## Containers and Pods

<table>
  <tr>
    <td><img src="icons/svg/container.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container.md">Container</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/pod.svg" width="50px;" alt=""/></td>
    <td><a href="docs/pod.md">Pod</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/pods.svg" width="50px;" alt=""/></td>
    <td><a href="docs/pods.md">Pods</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/pod-spec-file.svg" width="50px;" alt=""/></td>
    <td><a href="docs/pod-spec-file.md">Pod Spec File</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/container-runtime.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-runtime.md">Container Runtime</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/deamon.svg" width="50px;" alt=""/></td>
    <td><a href="docs/deamon.md">Deamon</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/container-close-look.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-close-look.md">Container Close Look</a></td>
  </tr>
</table>

## Deployment

<table>
  <tr>
    <td><img src="icons/svg/deployment.svg" width="50px;" alt=""/></td>
    <td><a href="docs/deployment.md">Deployment</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/replica-set.svg" width="50px;" alt=""/></td>
    <td><a href="docs/replica-set.md">Replica Set</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/stateful-set.svg" width="50px;" alt=""/></td>
    <td><a href="docs/stateful-set.md">Stateful Set</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/deamon-set.svg" width="50px;" alt=""/></td>
    <td><a href="docs/deamon-set.md">Deamon Set</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/cron-job.svg" width="50px;" alt=""/></td>
    <td><a href="docs/cron-job.md">Cron Job</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/job.svg" width="50px;" alt=""/></td>
    <td><a href="docs/job.md">Job</a></td>
  </tr>
</table>

## Networking

<table>
  <tr>
    <td><img src="icons/svg/admissions-controller.svg" width="50px;" alt=""/></td>
    <td><a href="docs/admissions-controller.md">Admissions Controller</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/network-policy.svg" width="50px;" alt=""/></td>
    <td><a href="docs/network-policy.md">Network Policy</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/ingress.svg" width="50px;" alt=""/></td>
    <td><a href="docs/ingress.md">Ingress</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/service.svg" width="50px;" alt=""/></td>
    <td><a href="docs/service.md">Service</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/headless-service.svg" width="50px;" alt=""/></td>
    <td><a href="docs/headless-service.md">Headless Service</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/ip-tables.svg" width="50px;" alt=""/></td>
    <td><a href="docs/ip-tables.md">IP Tables</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/ipvs.svg" width="50px;" alt=""/></td>
    <td><a href="docs/ipvs.md">IPVS</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/endpoint-slice.svg" width="50px;" alt=""/></td>
    <td><a href="docs/endpoint-slice.md">Endpoint Slice</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/endpoint.svg" width="50px;" alt=""/></td>
    <td><a href="docs/endpoint.md">Endpoint</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/proxy.svg" width="50px;" alt=""/></td>
    <td><a href="docs/proxy.md">Proxy</a></td>
  </tr>
</table>

<table>
  <tr>
    <td><img src="icons/svg/flux.svg" width="50px;" alt=""/></td>
    <td><a href="docs/flux.md">Flux</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/argo.svg" width="50px;" alt=""/></td>
    <td><a href="docs/argo.md">Argo</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/nginx-ingress-controller.svg" width="50px;" alt=""/></td>
    <td><a href="docs/nginx-ingress-controller.md">Nginx Ingress Controller</a></td>
  </tr>
</table>

## Storage

<table>
  <tr>
    <td><img src="icons/svg/core-dns.svg" width="50px;" alt=""/></td>
    <td><a href="docs/core-dns.md">Core DNS</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/persistent-volume-claim.svg" width="50px;" alt=""/></td>
    <td><a href="docs/persistent-volume-claim.md">Persistent Volume Claim</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/persistent-volume.svg" width="50px;" alt=""/></td>
    <td><a href="docs/persistent-volume.md">Persistent Volume</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/ephemeral-storage.svg" width="50px;" alt=""/></td>
    <td><a href="docs/ephemeral-storage.md">Ephemeral StoragP</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/projected-volume.svg" width="50px;" alt=""/></td>
    <td><a href="docs/projected-volume.md">Projected Volum</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/volume-snapshot.svg" width="50px;" alt=""/></td>
    <td><a href="docs/volume-snapshot.md">Volume Snapshot</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/storage-class.svg" width="50px;" alt=""/></td>
    <td><a href="docs/storage-class.md">Storage Class</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/secrets.svg" width="50px;" alt=""/></td>
    <td><a href="docs/secrets.md">Secrets</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/config-map.svg" width="50px;" alt=""/></td>
    <td><a href="docs/config-map.md">Config Map</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/etcd.svg" width="50px;" alt=""/></td>
    <td><a href="docs/etcd.md">Etcd</a></td>
  </tr>
</table>

## Role Based Access Controls (RBAC)
<table>
  <tr>
    <td><img src="icons/svg/role.svg" width="50px;" alt=""/></td>
    <td><a href="docs/role.md">Role</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/role-binding.svg" width="50px;" alt=""/></td>
    <td><a href="docs/role-binding.md">Role Binding</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/cluster-role.svg" width="50px;" alt=""/></td>
    <td><a href="docs/cluster-role.md">Cluster Role</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/cluster-role-binding.svg" width="50px;" alt=""/></td>
    <td><a href="docs/cluster-role-binding.md">Cluster Role Binding</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/service-account.svg" width="50px;" alt=""/></td>
    <td><a href="docs/service-account.md">Service Account</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/user.svg" width="50px;" alt=""/></td>
    <td><a href="docs/user.md">User</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/group.svg" width="50px;" alt=""/></td>
    <td><a href="docs/group.md">Group</a></td>
  </tr>
</table>

## Open Standards

<table>
  <tr>
    <td><img src="icons/svg/container-storage-interface.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-storage-interface.md">Container Storage Interface</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/container-network-interface.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-network-interface.md">Container Network Interface</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/container-runtime-interface-container-d.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-runtime-interface-container-d.md">Container Runtime Interface (ContainerD)</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/container-runtime-interface-cri-o.svg" width="50px;" alt=""/></td>
    <td><a href="docs/container-runtime-interface-cri-o.md">Container Runtime Interface (CRI-O)</a></td>
  </tr>
</table>

## Autoscaling and Limits

<table>
  <tr>
    <td><img src="icons/svg/vertical-pod-autoscaler.svg" width="50px;" alt=""/></td>
    <td><a href="docs/vertical-pod-autoscaler.md">Vertical Pod Autoscaler</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/horizontal-pod-autoscaler.svg" width="50px;" alt=""/></td>
    <td><a href="docs/horizontal-pod-autoscaler.md">Horizontal Pod Autoscaler</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/cluster-autoscaler.svg" width="50px;" alt=""/></td> 
    <td><a href="docs/cluster-autoscaler.md">Cluster Autoscaler</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/limit-range.svg" width="50px;" alt=""/></td>
    <td><a href="docs/limit-range.md">Limit Range</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/resource-quotas.svg" width="50px;" alt=""/></td>
    <td><a href="docs/resource-quotas.md">Resource Quotas</a></td>
  </tr>
</table>

## Kubelet

<table>
  <tr>
    <td><img src="icons/svg/kubelet.svg" width="50px;" alt=""/></td>
    <td><a href="docs/kubelet.md">Kubelet</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/readiness-probe.svg" width="50px;" alt=""/></td>
    <td><a href="docs/readiness-probe.md">Readiness Probe</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/liveness-probe.svg" width="50px;" alt=""/></td> 
    <td><a href="docs/liveness-probe.md">Liveness Probe</a></td>
  </tr>
  <tr>
    <td><img src="icons/svg/startup-probe.svg" width="50px;" alt=""/></td>
    <td><a href="docs/startup-probe.md">Startup Probe</a></td>
  </tr>
</table>
