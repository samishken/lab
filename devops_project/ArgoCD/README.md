# ARGOCD

#### Install
- https://argo-cd.readthedocs.io/en/stable/getting_started/
- - kubectl create namespace argocd
- - kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

- - To pull initial password 
- - - - `kubectl get secrets -n argocd`
- - - - `kubectl edit secret argocd-initial-admin-secret -n argocd`
- - - - `echo passwordvalue== | base64 --decode`  echo aHdFOHNiYWpZRWlIRzVBeQ== | base64 --decode

#### Connect EKS cluster to ArgoCD

-- Create Application