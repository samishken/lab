# Storage for EKS Cluster

## Scenario:
- You're deploying a PostgreSQL database in EKS to serve as the backend for a web application (say, an e-commerce app). You want the database's data to persist even if the pod or node crashes. So, you use an EBS-backed PersistentVolume.
- Example, The Business Need
You're building a scalable e-commerce platform (like Shopify or Amazon) hosted on AWS. Your application is deployed on Amazon EKS, and it needs to:
    - a) Store customer data (e.g., usernames, emails)
    - b) Manage product inventory
    - c) Handle orders, payments, and shipping info
    - d) Maintain transactional integrity (ACID compliance)
    - e) survive crashes or rescheduling of pods

** For all of this, you need a reliable, persistent relational database — and you choose PostgreSQL. **
---
#### Why You Need EBS-backed Storage
Containers and pods in Kubernetes are ephemeral — they can be destroyed and recreated anytime due to:

    - Node failures
    - Pod eviction or rescheduling
    - Cluster upgrades
    - Scaling operations
    - If you store your PostgreSQL data in the container’s local storage (emptyDir or container filesystem), you’ll lose all data when the pod is restarted or moved.
    - EBS solves this by providing persistent, block-level storage that is:
    - Durable (data survives pod crashes)
    - Reliable (backed by AWS SLAs)
    - High-performance (gp3/io2 options for IOPS)
---

### PVC: persistent volume claim

### EBS Volume (elastic bloack storage)
- mount on eks


### StatefulSet
- Creates N number of replicas for pods and persistent volumes.
- Each pod will have it's own ppersistent volume and persistent volumes claim storage. Each pod will have it's own storage.
- if the pod goes away, the volume, the data will remain until another pod is recreated.

### Deployment
- Creates N number of replicas, scales using HPA.
- In deployment case all pods share the same persistent volume using the same persistent volume claim.
- All pods share the same storage.

### Daemonset
- Deploys one or multiple pods in each node of the cluster.  Example poos that we want to deplploy on all nodes will be the ones that collect logs, metrics, and configure network policies.

---
### Static Provisioning of Persistent Volume
- Step 1: Create an EBS volume using AWS CLI:
    ```
    aws ec2 create-volume --size 10 --region us-east-1 --availability-zone us-east-1a --volume-type gp2
    ```
- Step 2: Get the volume ID from the output and replace in the following YAML
```
cat <<EOF | kubectl apply -f -
# Create a PersistentVolume (PV)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: ebs-pv
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  csi:
    driver: ebs.csi.aws.com
    fsType: ext4
    volumeHandle: <vol-id>    ##### add volume id here
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: topology.kubernetes.io/zone
              operator: In
              values:
                - us-east-1a
---
# Create a PersistentVolumeClaim (PVC)
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ebs-pvc
spec:
  storageClassName: ""
  volumeName: ebs-pv
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
---
# Create a pod using the PVC
apiVersion: v1
kind: Pod
metadata:
  name: ebs-pod
spec:
  nodeSelector: 
    topology.kubernetes.io/zone: us-east-1a
  containers:
  - name: app
    image: busybox
    command: [ "sh", "-c", "echo Hello Kubernetes! && sleep 3600" ]
    volumeMounts:
    - mountPath: "/data"
      name: ebs-storage
  volumes:
  - name: ebs-storage
    persistentVolumeClaim:
      claimName: ebs-pvc
EOF
```

--- 

### Create a Default Storage Class
- Create a default storage class for dynamic provisioning.
```
    cat <<EOF | kubectl apply -f -
    # Create a StorageClass
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
    name: ebs-sc
    provisioner: ebs.csi.aws.com
    volumeBindingMode: WaitForFirstConsumer
    EOF
```

### Create Pod to Use new Storage Class
- Create new PVC to use the default storage class and deploy new pod.

```
cat <<EOF | kubectl apply -f -
# PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ebs-pvc-new
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 10Gi
```

```
    # Re-deploy pod
    apiVersion: v1
    kind: Pod
    metadata:
    name: ebs-pod-new
    spec:
    containers:
    - name: app
        image: busybox
        command: [ "sh", "-c", "echo Hello Kubernetes! && sleep 3600" ]
        volumeMounts:
        - mountPath: "/data"
        name: ebs-storage
    volumes:
    - name: ebs-storage
        persistentVolumeClaim:
        claimName: ebs-pvc-new
    EOF
```
