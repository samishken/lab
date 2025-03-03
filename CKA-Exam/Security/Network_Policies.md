# Network Policies
- allows users to restrict desired communications.
- The pods should be able to communicate with each other without having to configure any additional settings like routes.
Traffic (simple ingress & egress setup)
- - web server (frontend) user sent in a request to web server at port 80. user then send a request to Backend server at port 5000.
- - App server (BackEnd): The api server fetches data from database server at port 3306 and sends the data back to the user.
- - database

### ingress
- Incoming traffic

### egress
- Outgoing traffic

### Each node has an IP address, as well as pods and services

- network policy rule



--- 
# Developing network policies
- FIRST create kind -> NetworkPolicy
- SECOND associate the policy with the pod that we want to protect.

    - -   NetworkPolicy associated with 'db' pod
        ```
            policyTypes:
            - Ingress
            - Egress
            ingress:
            - from:
            podSelector:
            matchLabels:
                role: db   (name: api-pod)
            ports:
            - protocol: TCP
                port: 3306
        ```

    - - db Pod
        ```
            labels:
            role: db 
        ```
- THIRD allow api server (backend) to quiery db pod (db server)

    - -  Add api server to communicate with db pod. 

        ```
            apiVersion: networking.k8s.io/v1
            kind: NetworkPolicy
            metadata:
                name: db-policy
            spec:
                podSelector:
                    matchLabels:
                    role: db
                policyTypes:
                - Ingress
                ingress:
                - from:
                    - podSelector:
                        matchLabels:
                        name: api-pod
                      namespaceSelector:
                        matchLabels:
                            name: prod
                    ports:
                    - protocol: TCP
                    port: 3306
        ```
