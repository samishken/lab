# Horizontal Pod Autoscaler (HPA) in Kubernetes - add pods

## What is HPA?

**Horizontal Pod Autoscaler (HPA)** is a Kubernetes resource that automatically scales the number of pods in a deployment, replica set, or stateful set based on observed **CPU utilization** or other select **custom metrics**.

HPA helps maintain optimal performance and resource usage by automatically adjusting the number of pod replicas based on demand.

---

## Key Features

- **Automatic scaling** based on metrics (CPU, memory, or custom metrics via the Metrics Server or external metrics providers).
- Works with **Deployment**, **ReplicaSet**, and **StatefulSet** resources.
- Supports scaling up and down within a defined range.

---
## Limitations
- Doesn’t scale based on queue length (consider `KEDA` or `custom metrics` for that).
- Not ideal for very fast scaling needs (reaction time depends on metrics collection interval).

---

## How It Works

1. Metrics (like CPU or memory usage) are collected via the **Metrics Server**.
2. The HPA controller compares current resource usage with the target utilization.
3. Based on the result, it adjusts the number of pod replicas accordingly.

---

## Example YAML

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: example-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## Useful Commands
```
# View current HPA status
kubectl get hpa

# Describe HPA for details
kubectl describe hpa <hpa-name>

```

