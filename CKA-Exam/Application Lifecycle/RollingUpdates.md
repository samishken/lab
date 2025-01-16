# Rollout
To get history of deployment
- `kubectl rollout status deployment/myapp-deployment`
- Rollback (Undo) `kubectl rollout undo deployment/myapp-deployment`

## Deployment Strategy
###### Rolling Update
- default deployment strategy
- replacing pods one by one (not updating all at once)
- To update deployment `kubectl apply -f deployment-definition.yml`
- or we can also update image -> `kubectl set image deployment/myapp-deployment nginx-container=nginx:1.7.1`
- `kubectl set image deployment/<deployment-name> <container-name>=<image-name>`

