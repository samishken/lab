## k run -h | less
## k run -h | vim

# kubectl run nginx --image=nginx --dry-run=client -o yaml > nginx.yaml

'communicate with the pod'
# "k exec -it nginx -- /bin/bash"
# "cat /etc/os-release"  to find out which OS is being used.

# k port-forward pod/mealie-bd5b5b597-97xzq 9000  [localhost:9000]