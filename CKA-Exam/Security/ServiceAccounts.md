# Service Account
- are used by machines
- monitoring application using service Account to pull Kubernetes API for performance metrics.
- For every namespace in kubernetes, a service account named default is automatically created.
- Each namespace has it's own default service account.

- To create SA `kubectl create serviceaccount dashboard-sa`
- - First creates SA object, then generates a token for SA, finally creates secret objects and stores the token.
- - The token is created automatically. Token is stored as secret object -> "dashboard-sa-token-kbbdm"
- - The SA token is what must be used by the external application to authenticate to Kubernetes API.
- To view SA `kubectl get serviceaccount`
- describe `kubectl describe serviceaccount dashboard-sa`
- The secret token is mouted at "/var/run/secrets/kubernetes.io/serviceaccount" inside the pod.
- `kubectl exec -it my-kuberenetes-dashboard -- ls /var/run/secrets/kubernetes.io/serviceaccount`
- - returns "ca.crt namespace token"
- `kubectl exec -it container-name -- cat /var/run/secrets/kubernetes.io/serviceaccount token` return token information
- - To view token `kubectl describe secret dashboard-sa-token-kbbdm`