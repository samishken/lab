# Helm HandsOn

### Installation
- Helm version 3

### How Helm selects which cluster to install packages?
- Helm looks for `current-contest` to install it's packages.
- Helm will install on the cluster that is the result of this query -> `kubectl config current-context`

### Helm repository
- **bitnami** is the repository. **nginx** is the chart. **nginx-v1** is the release information
-  `helm install nginx-v1 bitnami/nginx` 
- A ***Helm repository*** is a collection of packaged Helm charts (called `.tgz` files) that are made available for others to use. It works like a package repository (e.g., apt or yum) but for Kubernetes applications.

You can add a Helm repository using:

```
helm repo add <repo-name> <repo-url>
```

After adding, you can search and install charts from that repository. Popular public Helm repositories include [Artifact Hub](https://artifacthub.io/) and Bitnami.
`helm repo add <repo-name> <repo-url>`

### Helm Chart
- A ***Helm chart*** is a collection of files that describe a set of Kubernetes resources. It acts as a package for your Kubernetes application, similar to a DEB or RPM file in Linux.
- *https://artifacthub.io/* enables finding, installing, and publishing Helm charts (similar to Docker Hub)

#### Creating a Chart:
- `helm` create myapp`
- This generates a new chart structure under the myapp directory.

#### Installing a Chart:
- `helm install my-nginx bitnami/nginx`
- Charts enable you to define complex applications, including deployments, services, config maps, and more, all bundled together for easy management.