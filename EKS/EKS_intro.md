# Introduction to Amazon EKS

Amazon **Elastic Kubernetes Service (EKS)** is a fully managed Kubernetes service provided by AWS. It simplifies running Kubernetes workloads by handling the setup of the **control plane**, **security**, and **high availability**, allowing you to focus on managing your applications.

### what comes with EKS cluster when we create it besides control and data planes?
* OIDC Endpoint
- - - - OIDC give us authentication for things that want to call into the cluster and integrate into AWS.
- - - - We use it to to map ourself to IAM identities.
* add-ons
* logging -> aws cloudwatch
* authentication -> configmaps

### What connects the control plane to the data plane?
The EKS control plane connects to the worker nodes using:
- The Kubernetes API (via public or private endpoint)
- IAM authentication and TLS for secure communication
- The control plane talks to the nodes using the **Kubelet** and **Kube Proxy** running on those nodes.
- Communication happens over **HTTPS (port 443)**, and traffic can go over the **public internet** or **private VPC endpoints**, depending on configuration.
Would you like this saved as a .md file or added to a document?

---

## 🧠 EKS Architecture Overview

### 1. **Control Plane** (Managed by AWS)
- Consists of Kubernetes components like API server, etcd, scheduler, and controller manager.
- Runs across multiple **Availability Zones (AZs)** for high availability.
- AWS handles scaling, patching, and maintenance of the control plane.
- In a region we'll see these components in different AZ's
- - etcd
- - api server
- - scheduler
- - controller mangers


### 2. **Data Plane** (Customer Managed)
- Made up of **EC2 worker nodes** or **Fargate** tasks that run your containers (pods).
- These nodes register with the EKS control plane to form the cluster.

### 3. **VPC & ENI Integration**
- EKS worker nodes run inside a **VPC**.
- Each node gets an **ENI (Elastic Network Interface)** to connect to the VPC.
- **Pods** running on the nodes are assigned **secondary IPs** from the VPC subnet via ENIs using the **AWS VPC CNI plugin**.

---

## 🖼️ EKS Architecture Diagram

![EKS Control Plane, Data Plane, VPC, and ENI](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2020/04/10/eks_architecture.png)

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

