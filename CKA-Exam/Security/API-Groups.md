# API Groups for kluster functionality
##### `apiVersion`
##### Groups: core and named group
- Core Group: /api/v1 (namespaces, pods, rc, events, endpoints, nodes, bindings, PV, PVC, configmaps, secrets, services)
- Named Group: /apis (/apps, /extenstions, /networking.k8s.io, /storage.k8s.io, /authentication.k8s.io)

# `curl http://localhost:6443 -k`
# `kubectl proxy`
