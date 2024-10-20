## vimrc

# kubectl reference from k8s documentation
https://kubernetes.io/docs/reference/kubectl/generated/kubectl/

## Pod
-- A pod is the smallest element on a k8s cluster
--- "kubectl run nginx --image=nginx --dry-run=client"
--- To comunicate with the pod "k exec -it nginx -- /bin/bash"
--- 'htop' command helps us see the thing running inside pods
-------- contains information about storage and netwroking
-------- to get detailed information about a particulat pod "k get pod nginx -o yaml less"
-- A pod is a collection of containers & other resources
---- Single container
---- Multi container
---- Init container



# Storage
# Networking


