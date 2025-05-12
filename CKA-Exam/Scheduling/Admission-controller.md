# Admission controllers

kubectl (~/.kube/config) -> Authentication process done through certificates -> Authorization (RBAC) -> *** `Admission Controller` ***-> kube apiserver -> create pod

- Admition contollers: help us implement better security measures to enforce how a cluster is used.

### Admission contoller types
- AlwaysPullImages
- DefaultStorageClass
- EventRateLimit
- NamespaceAutoProvision
- NamespaceExists: namespaces not found
- Example `kubectl run nginx --image nginx --namespace blue`
- message `Error from server (NotFound): namespaces "blue" not found`

### Working Admission contorollers
`kubernetes have NamespaceExists admission controller enabled which rejects requests to namespaces that do not exist. So, to create a namespace that does not exist automatically, we could enable the NamespaceAutoProvision admission controller Enable the NamespaceAutoProvision admission controller`

### Enable Admission Controllers
- `$ vi /etc/kubernetes/manifests/kube-apiserver.yaml`
```
Add NamespaceAutoProvision admission controller to --enable-admission-plugins list to /etc/kubernetes/manifests/kube-apiserver.yaml
It should look like below

    - --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
API server will automatically restart and pickup this configuration.

```



#### Disable DefaultStorageClass admission controller

`This admission controller observes creation of PersistentVolumeClaim objects that do not request any specific storage class and automatically adds a default storage class to them. This way, users that do not request any special storage class do not need to care about them at all and they will get the default one.`
<br>
- `Add DefaultStorageClass to disable-admission-plugins in /etc/kubernetes/manifests/kube-apiserver.yaml`
```
Update /etc/kubernetes/manifests/kube-apiserver.yaml as below

   - --disable-admission-plugins=DefaultStorageClass


```