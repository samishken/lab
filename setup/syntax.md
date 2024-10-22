- k run -h | less
- k run -h | vim
- `watch -n 1 "kubectl get pods"`  watch activity every second
- kubectl run nginx --image=nginx --dry-run=client -o yaml > nginx.yaml
- set current namespace for current working environment
---- "k config set-context --current --namespace=default"

'communicate with the pod'
# "k exec -it nginx -- /bin/bash"
# "cat /etc/os-release"  to find out which OS is being used.

# k port-forward pod/mealie-bd5b5b597-97xzq 9000  [localhost:9000]

<!-- Forwarding from 127.0.0.1:9000 -> 9000
Forwarding from [::1]:9000 -> 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000 -->