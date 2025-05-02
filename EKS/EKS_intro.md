# Introduction to Amazon EKS

Amazon **Elastic Kubernetes Service (EKS)** is a fully managed Kubernetes service provided by AWS. It simplifies running Kubernetes workloads by handling the setup of the **control plane**, **security**, and **high availability**, allowing you to focus on managing your applications.

---

## 🧠 EKS Architecture Overview

### 1. **Control Plane** (Managed by AWS)
- Consists of Kubernetes components like API server, etcd, scheduler, and controller manager.
- Runs across multiple **Availability Zones (AZs)** for high availability.
- AWS handles scaling, patching, and maintenance of the control plane.

### 2. **Data Plane** (Customer Managed)
- Made up of **EC2 worker nodes** or **Fargate** tasks that run your containers (pods).
- These nodes register with the EKS control plane to form the cluster.

### 3. **VPC & ENI Integration**
- EKS worker nodes run inside a **VPC**.
- Each node gets an **ENI (Elastic Network Interface)** to connect to the VPC.
- **Pods** running on the nodes are assigned **secondary IPs** from the VPC subnet via ENIs using the **AWS VPC CNI plugin**.

---

## 🖼️ EKS Architecture Diagram

![EKS Control Plane, Data Plane, VPC, and ENI](https://d1.awsstatic.com/diagrams/eks-control-data-plane.3fa7f86a73a32fdf3705e5f9f9806c12b0115e75.png)

**Image Source**: [AWS EKS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

---

## ✅ Key Benefits of EKS

- **Fully managed control plane** with automatic scalability and availability
- **Deep integration with AWS services** like IAM, VPC, ELB, and CloudWatch
- **VPC-native pod networking** using ENIs for direct access to AWS services
- **Support for EC2 and AWS Fargate** as compute backends

---

## 🧩 Summary

Amazon EKS abstracts away the complexity of managing Kubernetes infrastructure. It offers a scalable and secure way to run containerized workloads, with full AWS-native networking support via **VPC and ENIs**.

