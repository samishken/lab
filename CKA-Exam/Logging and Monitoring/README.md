# Logging and MOnitoring

## Kubernetes Logging
- HOW ARE THE METRICS GENERATED FOR pods on nodes?
- K8s runs an agent on each node known as the kubelet, which is responsible for receiving instructions 
from the k8s API Master server and running PODs on the Nodes.
- The kubelet also contains a subcomponent known as cAdvisor or Container Advisor.
- Container Advisor is responsible for retriving performance metrics from pods, and exposing them
through the kubelet API to make the metrics available for Metrics Server. 
- `kubectl top node` provides CPU and Memory consumption of each of the nodes.
- `kubectl top pod` provides CPU and Memory consumption of each of the pods.

## Kubernetes Logging
- `kubectl logs my-pod -c my-container -n my-namespace`
- `kubectl create -f event-simulator.yaml`
- `kubectl log -f event-simulator.yaml`
- If there are multiple containers in the pod created by `event-simulator.yaml` file, then
- `kubectl logs -f event-simulator.yaml CONTAINER_NAME`

## Docker Logging
- `docker log -f CONTAINER_ID`