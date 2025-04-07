# Json Path in KubeCtl

### why json path?
- 


### View and interpret KubeCtl output in JOSN Format

# Commands

- json output `kubectl get nodes -o json`
- json path query `.items[0].spec.containers[0].image`
- view users from config file file anem my-kube-config `kubectl config view --kubeconfig=my-kube-config --raw -o jsonpath='{.users[*].name}'`
- Get `osImages` of all nodes `kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.osImage}'`
- kubectl & json path query `kubectl get pods -o=jsonpath='{.items[0].spec.containers[0].image'}`
- `kubectl get nodes -o=jsonpath='{.items[*].metadata.name}'` - returns nodes in the cluster
- `kubectl get nodes -o=jsonpath='{.items[*].status.nodeInfo.architecture}'` - returns harware archi of nodes
- count of CPU's `kubectl get nodes -o=jsonpath='{.ites[*].status.capacity.cpu}'`
- combining two queries with new line `kubectl get nodes -o=jsonpath='{.ites[*].status.capacity.cpu} {"\n"} {.items[*].status.nodeInfo.architecture}'`
---
- Loop 
 ```
   '{range. items[*]}
        {.metadata.name} {"\t"} {.status.capacity.cpu} {"\n"}
    {end}'
 ```
- `kubectl get nodes -o=jsonpath='{range. items[*]}{.metadata.name} {"\t"} {.status.capacity.cpu} {"\n"}{end}'`
- side by side add {"\t"}
- add new line {"\n"}
- end the loop {"end"}

- `kubectl get nodes -o=custom-columns=<COLUMN NAME>: <JSON PATH>`
- `kubectl get nodes -o=custom-columns=<COLUMN NAME>:.metadata.name,CPU:.status.capacity.cpu`

- Sort by
- `kubectl get nodes --sort-by= .metadata.name`
- `kubectl get nodes --sort-by= .status.capacity.cpu`

