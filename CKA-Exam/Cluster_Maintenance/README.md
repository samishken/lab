# Cluster Maintenance
### Velero tool is used to backup k8s cluster
### ETCD: State of our cluster is stored in key/value format.
- Get etcd version `kubectl -n kube-system logs etcd-controlplane | grep -i 'etcd-version'`
- location for ECTC Server Certificate `/etc/kubernetes/pki/etcd/server.crt`
- Where is the ETCD CA Certificate file located?  `/etc/kubernetes/pki/etcd/ca.crt`
- To take backup follow these steps <br>
---- 1st) Stop kube-apiserver service `service kube-apiserver stop` <br>
---- 2nd) Snapshot restore
---- 3rd) update etcd configuration file to use the new data
---- 4th) reload and restart service
<br>
- `ectd.service` file
- `(--data-dir=/var/lib/etcd)`
    - 
    ```
    ETCDCTL_API=3 etcdctl \ 
    snapshot save snapshot.db`
    ```
- ls (`snapshot.db`)
- `service kube-apiserver stop`  => Service kube-apiserver stopped
    ```
    ETCDCTL_API=3 etcdctl \
    snapshot restore snapshot.db \
    --data-dir /var/lib/etcd-from-backup

    => I | mvcc: restore compact to 475629
    ```
- The master node in our cluster is planned for a regular maintenance reboot tonight. While we do not anticipate anything to go wrong, we are required to take the necessary backups. Take a snapshot of the ETCD database using the built-in snapshot functionality.
Store the backup file at location /opt/snapshot-pre-boot.db
- Take snapshot
    ```
        ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 \
        --cacert=/etc/kubernetes/pki/etcd/ca.crt \
        --cert=/etc/kubernetes/pki/etcd/server.crt \
        --key=/etc/kubernetes/pki/etcd/server.key \
        snapshot save /opt/snapshot-pre-boot.db
    ```
- Restore
    ```
    ETCDCTL_API=3 etcdctl  --data-dir /var/lib/etcd-from-backup \
    --cacert=/etc/kubernetes/pki/etcd/ca.crt \
    --cert=/etc/kubernetes/pki/etcd/server.crt \
    --key=/etc/kubernetes/pki/etcd/server.key \
    snapshot restore /opt/snapshot-pre-boot.db
    ```
- Update `/etc/kubernetes/manifests/etcd.yaml` file
---
- update `etcd.service` -> (`--data-dir=/var/lib/etcd-from-backup`)
    - `systemctl daemon-reload`
    - `service etcd restart`
    - `service kube-apiserver start` => service kube-apiserver started


##### Updating Nodes?
- when nodes go down the podes are not accessable? <br>
- If Nodes go down for less than 5 minutes, then then previous pods will come back. <br>
- If Nodes go down for more than 5 minutes, the pods within them will be terminated. <br>
- If the pods are set as replicasets, then the pods will start running on another node <br>
- Otherwise the pods will be evicted and terminated. <br>
- When the Nodes (which was down for over 5 minutes) come back, then it'll be empty <br>

##### Quick upgrade and reboot -> Drain the node
- `kubectl drain node-1`  -> distribute the pods to another nodes. No pods can be scheduled on this node <br>
- `kubectl cordon node-1` -> Pods will not be moved from the nodes. Prevents new pods to be scheduled on that node.
- `kubectl uncordon node-1` -> After the node restarts "uncordon" it so that pods can start scheuling on the node again

##### K8s versions
`v1.11.3`
- 1) v1: Major version <br>
- 2) 11: minor version <br>
- 3) 3: patch version <br>

##### Cluster update
- kubernetes components can have different versions <br>
- All components on Control plane must have equal or lower version <br>
- Upgrade one minor version at a time. <br>
- `kubeadm upgrade plan`, `kubeadm upgrade apply`, `kubeadm upgrade apply NEW-VERSION`
- For cloud envirornments <br>
- if we want to upgrade cluster version, create new Nodes with the latest version, drain old nodes one-by-one. <br>
- Steps To upgrade on "kubeadm" - https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
----- A) upgrade Master (controlplane) nodes <br>
- 1) `apt-get upgrade -y kubeadm=VERSION-NUMBER` <br>
- 2) `kubeadm upgrade apply VERSION-NUMBER` <br>
- 3) `kubectl get nodes`  still see old version because nodes were registered on the old kubernetes version. <br>
- 4) Upgrade "kubelets" on master node `apt-get upgrade -y kubelet=VERSION-NUMBER` <br>
- 5) `systemctl restart kubelet` <br>
- 6) `kubectl get nodes` should show the master being updated to latest version but the worker nodes still show old k8s version. <br>

--- 
----- B) upgrade Worker nodes <br>
- 7) `kubectl drain node-1` let's us move pods to different nodes. and make it that no pods can be scheduled on it <br>
----- 1) `apt-get upgrade -y kubeadm=VERSION-NUMBER` <br>
----- 2) `apt-get upgrade -y kubelet=VERSION-NUMBER` <br>
----- 3) `kubeadm upgrade node config --kubelet-version VERSION-NUMBER` <br>
----- 4) `systemctl restart kubelet` <br>
- 8) `kubectl uncordon node-1` after upgrading the node, make sure pods can be scheduled on this node <br>

Steps to upgrade Controlplane:
---
1) Find the latest patch release for kubernetes
- `sudo apt update`
- `sudo apt-cache madison kubeadm`
---
2) Upgrade kubeadm
```
sudo apt-mark unhold kubeadm && \
sudo apt-get update && sudo apt-get install -y kubeadm='1.31.0' && \
sudo apt-mark hold kubeadm
```
 - Verify version ```kubeadm version```
 - Verify upgrade plan ```sudo kubeadm upgrade plan``` : This command checks that your cluster can be upgraded, and fetches the versions you can upgrade to. It also shows a table with the component config version states.
 - Choose a version to upgrade to ```sudo kubeadm upgrade apply v1.31.x``` 
 - Once the command finishes you should see: ```[upgrade/successful] SUCCESS!```
 - if we have another node on control plane ```sudo kubeadm upgrade node``` instead of ```sudo kubeadm upgrade apply```
--- 
3) Drain the node
    ```
    `sudo kubeadm upgrade node`
    `kubectl drain node-1 --ignore-daemonsets`
    ```
---
4) Upgrade the kubelet and kubectl:
    ```
    sudo apt-mark unhold kubelet kubectl && \
    sudo apt-get update && sudo apt-get install -y kubelet='1.32.3-1.1' kubectl='1.32.3-1.1' && \
    sudo apt-mark hold kubelet kubectl
    ```
---
5)  Restart kubelet
    ```
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
---
6) Uncordon the node
    ```
    kubectl uncordon node01
    kubectl get node` should show the latest version
    ```
---
---
---
Steps to upgrade Worker nodes:
---
1) Find the latest patch release for kubernetes
- `sudo apt update`
- `sudo apt-cache madison kubeadm`
---
2) Call "kubeadm upgrade": For worker nodes this upgrades the local kubelet configuration
    ```
    sudo kubeadm upgrade node
    ```
--- 
3) Drain the node
    ```
    `kubectl drain node-1 --ignore-daemonsets`
    ```
---
4) Upgrade the kubelet and kubectl:
    ```
    sudo apt-mark unhold kubelet kubectl && \
    sudo apt-get update && sudo apt-get install -y kubelet='1.32.3-1.1' kubectl='1.32.3-1.1' && \
    sudo apt-mark hold kubelet kubectl
    ```
---
5)  Restart kubelet
    ```
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
---
6) Uncordon the node: `kubectl get node` should show the latest version
    ```
    kubectl uncordon node01
    ```

