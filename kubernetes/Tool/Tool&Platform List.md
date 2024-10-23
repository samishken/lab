# Autoscaler
- Karpenter (helps keep cost down and it's much faster than cluster autoscaler)

# Service Mesh
- Istio (for encryption, for troubleshooting, and network latency)

# Monitoring and Observability
- Prometheus and Grafana: open source
- Datadog (Enterprise is better otherwise we will deal with lots of tools and a lot of open source that we have to manage. Teams don't have the man power.)
----- Monitoring
----- Logging
----- Traces
----- Metrics
----- API

# OIDC
- AWS IAM (RBAC, Authentication authorization)

# Cluster Deployment
- Terraform

# App Deployment
- GitOps (ArgoCD)

# Secret Manager
- Hashicorp Vault

# Failover and DR
- Velero or EBS snapshots

# Scanner
- kubescape

## Cost and Resource Optimization
(To keeping costs low & ensuring that the resources, memory, CPU etc are available and what's needed for our cluster, we don't want to over utilize and we certainly don't want to under utilize if we under utilize our applications are not performing as expected. If we over utilize, we have a cost problem.)

- Sosivio
- Cast.ai