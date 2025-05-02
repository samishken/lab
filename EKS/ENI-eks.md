## What are ENIs in EKS?

In **Amazon EKS (Elastic Kubernetes Service)**, **ENI** stands for **Elastic Network Interface**. It is a virtual network interface that provides network connectivity for resources in a VPC, and it's crucial for how EKS pods communicate within and outside the cluster.

---

### 📌 Role of ENIs in EKS

#### 1. Pod-Level Networking with VPC CNI Plugin

- EKS uses the **AWS VPC CNI plugin** by default.
- Each **pod** receives an IP address from the **VPC subnet**, enabling it to communicate directly with other AWS services or across VPCs.
- These pod IPs are assigned as **secondary IP addresses** to the EC2 instance’s ENIs.

📷 **EKS Networking Model**  
![EKS VPC CNI plugin model](https://docs.aws.amazon.com/eks/latest/userguide/images/eks-vpc-cni.png)

---

#### 2. ENIs per Node

- Every EC2 instance (EKS worker node) has:
  - A **primary ENI** for node-level communication.
  - **Secondary ENIs** and IP addresses used by pods.
- The number of ENIs and secondary IPs varies based on the **instance type**.

📷 **ENIs and IPs per Node Type**  
![ENI and IP limit per instance type](https://docs.aws.amazon.com/eks/latest/userguide/images/eni_limits.png)

> You can also refer to [this ENI limits table](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI) for detailed instance limits.

---

#### 3. Custom Networking (Optional)

- EKS supports **custom networking**, where pods can get ENIs from different subnets for better **isolation** and **security**.
- This can be used to assign pods different **security groups**, **subnets**, or **routing policies**.

📷 **Custom Networking in EKS**  
![Custom networking architecture](https://d1.awsstatic.com/blog/2021/containers/eks-custom-networking/custom-networking-diagram.1fc0e735420ffb10da4d68281816f7471fa9a39a.png)

---

### ✅ Benefits of ENI-Based Networking in EKS

- **VPC-native networking** (no overlay)
- **Direct access** to AWS services (e.g., S3, RDS)
- **Improved security** via security groups per ENI
- **Better scalability** tied to EC2 instance type limits

---

### 🔁 Summary

- ENIs are key to how EKS provides **pod-level networking**.
- Managed automatically by the **VPC CNI plugin**.
- Enable seamless integration between **Kubernetes networking** and **AWS infrastructure**.
