# Scheduling
- In Kubernetes, scheduling means making sure that pods are attached to worker nodes.
- Kubernetes scheduling is the process of assigning pods to nodes in a cluster so that Kubelet can run them

### Manually Schedule Pod to Specific Node
- Add `nodeName` to assign pod to specific node manually
##### Here is an example of a Pod spec using the nodeName field:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01
  ```


### Labels & Selectors (Annotations)
- methods to group things (kubernetes objects) together. Like Pods, services, ReplicaSets, Deployments
- Groups object by type, by application (app1, app2, app3) or by their functionality. Example: front-end, back-end, db, audit, image-processing, video-processing, auth, web-servers, app-server.
- `kubectl get pods --selector app=App1`
- `kubectl get pods --selector app=App1,bu=finance,tier=frontend`
- Annotations: are used to record details for informatory purpose.


### Taints & Tolerations
- By default the Control plane (master node) comes with taint so pods are not going to be scheduled on it.
- `kubectl describe node kubemaster | grep Taint`
- This is a way to instruct Nodes to accept pods with certain tolerations 
- Taint: are set on Nodes. We add taints on Nodes so that selective pods can be scheduled
---- `kubectl taint nodes node-name key1=value1:taint-eff`
---- Taint Effect Types,,,,  find out what they are ```NoSchedule | PreferNoSchedule | NoExecute```
---- `kubectl taint nodes node1 app=blue:NoSchedule`
- Tolerations: are set on Pods. We add tolerations to Pods so that pods can be scheduled on tainted Node.

```
##### Toleration - Pod
##### `kubectl taint nodes node1 app=blue:NoSchedule`
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "blue"
    effect: "NoSchedule"
```

### Node Selectors
- `nodeSelector`
- Label nodes and add `nodeSelector` in our Pod definition file after containers
- To Label Nodes:
---- `kubectl label nodes <node-name> <label-key>=<label-value>` 

### Node Affinity
- ensure pods are placed in particular nodes.
##### Node Affinity operators
- Exists
- In
- NotIn

##### Node Affinity types 

##### Available:
- - If changes made to Node label there won't be an issue in this case
---- When creating a pod if we require the scheduler to place it on a specific node
- `requiredDuringSchedulingIgnoredDuringExecution:` (node must have a matching label)
---- When creating a pod if we are less interested in selecting a specific node.
- `preferredDuringSchedulingIgnoredDuringExecution:` (label on node is not neccessary)
- During Scheduling: when a pod is created for the first time.
- During Execution: pod has been running and a node label change was made 

##### Planned:
- In the following cases, the pod and node must have the same lable.  
- If changes made to Node label, then the pods will be removed from the node.
- `requiredDuringSchedulingRequiredDuringExecution:`
- `preferredDuringSchedulingRequiredDuringExecution:`


### Node Affinity vs Taints and Torations 
- To fulfill this task we follow these steps
- Apply Taints on the nodes
- Add then add Node Affinity Pods

### Resource Limits & Requests  (*** Review this section Again ***)
- CPU & Memory limits
- The Scheduler takes into consideration the amount of resources required by a pod and those available on the nodes and identifies the best node to place a pod on. 


## Resource LimitRange
- A LimitRange is used to enforce default resource limits and constraints on a namespace, such as CPU, memory requests, and limits for pods or containers.

## Resource Quotas
- A ResourceQuota is used to set constraints on the total resource consumption within a namespace, such as CPU, memory, and object counts.


## DaemonSets
- DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them.
- DaemonSets helps us deploy multiple instances of pod. But it runs one copy of Pod on each Node in the cluster.
- DaemonSets are used when a single copy of an application must run on all or a subset of the nodes in the cluster. 
- DaemonSets are often used for system-level services, like proxies or load balancers, that need to run on every node. 
- DaemonSets automatically scale when nodes are added or removed from the cluster.
- Use Case: If we want to add a monitoring agent or log collector for each of the node in the cluster.
- `kubernetes get daemonset -A -o wide`

## Static Pods
- Static Pods are managed directly by the kubelet daemon on a specific node, without the API server observing them.
- In the case of no Master Node, Add the pod definition file in this directory `/etc/kubernetes/manifests`
- To configure `--pod-manifest-path=/etc/kubernetes/manifests`
- Best way to configure
------ Check "kubelet.service" file to see if `--config=kubeconfig.yaml` exists
------ kubeconfig.yaml (`staticPodPath: /etc/kubernetes/manifests`)
------ Use `docker ps` command to manage created Pods
- ###### Static Pod Use Case
- Can be used to create multiple Master nodes (controlplane)
- Can be used to Deploy controlplane components as Static Pods
- `kubectl ssh node NODE_NAME`


## Deploying Multiple Schedulers
- Default scheduler is configured in `scheduler-config.yaml`
- my-scheduler-2-config.yaml
```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- scheduleName: my-scheduler-2
leaderElection:
  leaderElect: true
  resourceNamespace: kube-system
  resourceName: lock-object-my-scheduler
```
## Scheduler Profile
- A scheduling Profile allows you to configure the different stages of scheduling in the kube-scheduler.