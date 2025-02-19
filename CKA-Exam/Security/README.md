# Security 

### k8s Security Primitives
- Password based authentication disabled
- ssh key based authentication
- "kube-apiserver" first line of defense
- who can access the cluster?  (Humans [Admins, Developers], Service Accounts [3rd party tools])
- what can they do once they get access?  RBAC Autherization - 
---
### Authentication
- control access to k8s cluster with authentication
- k8s only let us create Service Accounts but not user access
- "kube-apisever" can authenticate using LDAP, Certificates
---
### TLS Certificates
- what are TLS certificates? <br>
- - - A certificate is used to guarantee trust between two parties during a transaction. <br>
- - - Symmetric Encyption: only only key used to authenticate access. <br>
- - - Asymmetric Encryption: pair of keys to (private and public) used to authenticate access <br>
- - - For Encryption, it's best to used asymmetric encryption with a pair of public and private keys <br>
- - - Admin uses a pair keys to secure SSH connectivity to the  servers.  The server uses a pair of keys to secure HTTPS traffic. <br>
- - - PKI (Public key Infastructure) is the process of issuing, validating, maintaining certificates, as well as all the CAs, involved servers <br>

---
- Types of Certificates (.crt, .pem): <br>
- - - Server certificates - configured on servers: <br>
- - - Root certificates - configured on CA servers: <br>
- - - Client certificates - configured on clients: <br>

---
- How does Kubernetes use certificates? <br>
* * 1) Automatically PKI gets generated under `/etc/kubernetes/pki` path when we lauch "KUBEADM". Auto generated CA
* * 2) 
---- all services within the cluster use Server certificates. <br>
---- all clients within the cluster use client certficates. <br>
- - Server certificates: <br>
- - - kube-api server (controlplan) <br> 
- - - ETCD server (controlplan) <br>
- - - kubelet server (worker node) <br>
- - Client certificates: <br>
- - - Admin user (need private and public key) <br>
- - - kube-scheduler: need client certificate to authenticate to API-Server <br>
- - - kube-controller-manager: need client certificate to authenticate to API-Server <br>
- - - kube-proxy: need client certificate to authenticate to API-Server <br>
- - - kube-api-server: need client certificate to authenticate to ETCD-Server <br>
- - - kube-api-server: need client certificate to authenticate to kubelet server <br>

---
## we need at least one CERTIFICATE AUTHORITY (CA) in the cluster to sign all these certificates
---
- How to generate TLS certificates? <br>
- - Use "OpenSSL" tool to generate CERTIFICATE AUTHORITY <br>
- - - Steps for Server certificates: <br>
---- 1st) Create Private key to using openssl command `openssl genrsa -out ca.key 2048` <br>
---- 2nd) Generate Certificate Signing Request. Use openssl request command along with the created key  `openssl req -new -key ca.key -subj "/CN=KUBENETES-CA" -out ca.csr` <br>
---- 3rd) Sign the Certificates using "x509" command `openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt` <br>

---
- - - Steps for Client certificates: <br>
1st) admin user: <br> 
---- a) Create private key using openssl command. `openssl genrsa -out admin.key 2048` <br> 
---- b) Create CSR (Certificate Signing Request) [kube-admin is very important] `openssl req -new -key admin.key -subj "/CN=kube-admin" -out admin` <br> 
---- c) Generate Sign certificates: specify CA certificate and CA key-pair.  The signed certificate output to admin.crt file  `openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt` <br>


Decode the certificate `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout`
`journalctl -u etcd.service -l`
`kubectl logs etcd-master`


---



---

- How to configure TLS certificates?
- How to view TLS certificates?
- How to troubleshoot issues related to certificates?

--- 





### Authorization
### Images Security
### Network Policies
- control access between pods
### Secure Persistent key value store
### Security Contexts