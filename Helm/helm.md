# Helm
- package manager for Kubernetes.
- Just like APT helps you manage software packages on a Linux system, Helm helps you manage applications on a Kubernetes cluster.

### Helm steps
* Step 1) Add repo
* Step 2) Helm install

### Helm supports
1) helm update
2) helm uninstall
3) bundle/package application as helm chart so that other users use helm command to install the application. (ex. Grafana/Prometheus)

### Why Helm
#### Big problem that needed to be soldved
- `LINUX`
- Imagine when we want to install 10 packages in our servers (ex. nginx, apache, java, python)
- The steps we take to install these packages include 
- - - - Prepare shell script for each package to install. 
- - - - Make shell script compatible with different versions since different applications use different version of packages.
- - - - Maintain the script up to date. 
- - - `apt` has everything that is required to accomplish the above.
- `HELM`
- Using helm we don't have to create multiple yaml files.
- With HELM we don't need to create multiple scripts (ex. deployment, namespace, service account, statefulset, configmaps) to install prometheus, grafana, argoCD.

#### 1. Package Management
- APT manages DEB packages (like .deb files) on Linux.
- Helm manages Helm Charts (YAML files bundled together) in Kubernetes.

#### 2. Version Control
- APT can install specific versions of a package using:
- `sudo apt install nginx=1.18.0`
- Helm can do the same:
- `helm install my-nginx bitnami/nginx --version 13.0.0`
- This means you can easily roll back or upgrade applications.

#### 3. Configuration Management
- With APT, you can configure software via config files (like /etc/nginx/nginx.conf).
- With Helm, you can override configuration values using a YAML file:
- `helm install my-nginx bitnami/nginx --values custom-values.yaml`
- This allows you to customize how the application is deployed.

#### 4. Managing Dependencies
- APT automatically resolves dependencies between packages.
- Helm handles dependencies between Kubernetes components, like ensuring a database is ready before deploying a web app.

#### Why Helm Matters in Kubernetes
Kubernetes is a complex system with many moving parts (pods, deployments, services, etc.). Helm simplifies the process by packaging everything into reusable charts. It’s like having a one-click install for your entire application stack instead of manually creating each component.
