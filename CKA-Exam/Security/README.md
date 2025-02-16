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
- what are TLS certificates?
---- A certificate is used to guarantee trust between two parties during a transaction.
---- Symmetric Encyption: only only key used to authenticate access.
---- Asymmetric Encryption: pair of keys to (private and public) used to authenticate access
---- For Encryption, it's best to used asymmetric encryption with a pair of public and private keys
---- Admin uses a pair keys to secure SSH connectivity to the servers.  The server uses a pair of keys to secure HTTPS traffic.
---- PKI (Public key Infastructure)


- How does Kubernetes use certificates?
- How to generate TLS certificates?
- How to ocnfigure TLS certificates?
- How to view TLS certificates?
- How to troubleshoot issues related to certificates?

--- 





### Authorization
### Images Security
### Network Policies
- control access between pods
### Secure Persistent key value store
### Security Contexts