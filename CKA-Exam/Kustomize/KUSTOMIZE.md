# Kustomize

### Install kustomize (k8s cluster must be running and kubectl must be installed)
- `curl "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash`

### why kustomize?
- modify attributes, to fit Different environments 

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