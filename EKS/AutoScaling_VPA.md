# Vertical Pod Autoscaling (VPA) in Kubernetes - make pods more powerful



## Overview

Vertical Pod Autoscaling (VPA) is a Kubernetes component that automatically adjusts the CPU and memory requests and limits of pods to help ensure they have the resources they need to run efficiently.

Unlike Horizontal Pod Autoscaling (HPA), which adjusts the number of pod replicas, VPA adjusts the **resource allocation** of individual pods.

## Key Features

- Recommends or automatically updates CPU and memory requests/limits.
- Helps avoid overprovisioning or underprovisioning.
- Useful for applications with variable resource usage or long-lived workloads.

## How It Works

1. **Recommender**: Monitors resource usage and provides recommendations.
2. **Updater**: Optionally evicts and restarts pods to apply updated resource values.
3. **Admission Controller**: Applies recommended values when pods are created or updated.

## Modes of Operation

- `Off`: VPA only makes recommendations.
- `Auto`: VPA updates resource requests and may evict pods to apply changes.
- `Initial`: VPA sets resource requests only at pod creation time.

## Use Cases

- Stateful applications (e.g., databases).
- Long-running batch jobs.
- Workloads with dynamic or unpredictable resource needs.

## Limitations

- Not suitable for deployments with frequent updates (can cause disruption due to pod restarts).
- Cannot be used together with HPA on the same metric (CPU/Memory).

## Example VPA Configuration

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Auto"  # "Recreate", "Initial", "Off"
```

---

## Update Modes:
- Auto: VPA automatically updates pods with new resource requests. It can use in-place updates (if available) or recreate the pods if necessary. 
- Recreate: VPA updates pods by evicting and recreating them when the resource requests change. 
- Initial: VPA only applies resource requests during pod creation and does not update existing pods. 
- Off: VPA provides recommendations but does not automatically update pods. 

--- 

