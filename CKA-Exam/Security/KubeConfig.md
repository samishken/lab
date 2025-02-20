# Security KUBECONFIG
- Default KUBECONFIG is located at `$HOME/.kube/config:` 
- 
- The kubeconfig file is a configuration file used by Kubernetes to authenticate and interact with a cluster. It contains details such as cluster information, user credentials, namespaces, and authentication tokens, allowing kubectl and other Kubernetes tools to communicate with the cluster.
- If KUBECONFIG is not configured properly it will use the default file

- Format of KUBECONFIG has three sections:
- - Clusters: various cluster we need access (Dev, Prod, Preprod)
- - Contexts: Define which User can access which clusters.
- - Users: Admin, dev user, Prod User

- KUBECONFIG important commands
- - `kubectl config view` - to view current config being used
- - `kubectl config view -kubeconfig=my-custom-config` 
- - To change Context `kbectl config use-context prod-user@production`
- - `kubectl config -h`

```
apiVersion: v1
kind: Config

clusters:
- name: my-cluster
  cluster:
    server: https://my-cluster-api-server:6443  # Kubernetes API server endpoint
    certificate-authority: /path/to/ca.crt  # CA certificate to verify the API server
    // certificate-authority-data: [add base64 information instead of the path]

contexts:
- name: my-context
  context:
    cluster: my-cluster
    user: my-user
    namespace: default  # Default namespace to use

current-context: my-context  # The context `kubectl` will use by default

users:
- name: my-user
  user:
    client-certificate: /path/to/client.crt  # Client certificate for authentication
    client-key: /path/to/client.key  # Private key for the client certificate

# Optional: Define multiple users, clusters, and contexts if needed

```
