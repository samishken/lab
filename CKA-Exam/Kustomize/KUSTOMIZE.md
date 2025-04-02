# Kustomize

### Install kustomize (k8s cluster must be running and kubectl must be installed)
- `curl "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash`

### why kustomize?
- modify attributes, to fit Different environments 

# kustomize build command
- print out what it will create `kustomize build k8s/`
- create`kustomize build k8s/ | kubectl apply -f -`  # 'k8s' is the name of the folder
- create `kubectl apply -k k8s/`
- delete `kustomize build k8s/ | kubectl delete -f -`
- delete `kubectl delete -k k8s/`

##### folder structure
- k8s/
- base/ # deployment manifest file
- - - - kustomization.yaml
- - - - nginx-depl.yml
- - - - service.yaml
- - - - redis-depl.yaml
- overlays
- - dev
- - - - kustomization.yaml
- - - - config-map.yaml
- - stage
- - - - kustomization.yaml
- - - - config-map.yaml
- - prod
- - - - kustomization.yaml
- - - - config-map.yaml


### Kustomize Transformers
- commonLabels
- namespace
- namePrefix
- commonAnnotations

