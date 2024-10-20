# Create deployment 
# kubectl create deploy test-deploy --image=httpd --replicas=5 --dry-run=client -o yaml > deploy.yaml

# replicasets

# strategy: 
--- Rolling: By default the strategy is set to be Rolling. Updates happen one or group after another
--- Recreate type will remove all at once and replace them.