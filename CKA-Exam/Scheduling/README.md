# Scheduling
- In Kubernetes, scheduling means making sure that pods are attached to worker nodes.
- Kubernetes scheduling is the process of assigning pods to nodes in a cluster so that Kubelet can run them

### Manually Schedule
- Add `nodeName` to assign pod to specific node manually
##### Here is an example of a Pod spec using the nodeName field:

```apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01


### Labels & Selectors (Annotations)
- methods to group things (kubernetes objects) together. Like Pods, services, ReplicaSets, Deployments
- Groups object by type, by application (app1, app2, app3) or by their functionality. Example: front-end, back-end, db, audit, image-processing, video-processing, auth, web-servers, app-server.
- `kubectl get pods --selector app=App1`
- Annotations: are used to record details for informatory purpose.



