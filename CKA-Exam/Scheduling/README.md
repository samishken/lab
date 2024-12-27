# Scheduling
- In Kubernetes, scheduling means making sure that pods are attached to worker nodes.
- Kubernetes scheduling is the process of assigning pods to nodes in a cluster so that Kubelet can run them

### Manually Schedule
- Add `nodeName` to assign pod to specific node manually
##### Here is an example of a Pod spec using the nodeName field:

`apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01`  

