# Helm

- Manifest files
- helm search
- helm pull  #pulls chart in archived format. we need to unarchive and customize
- helm get
- helm list
- helm rollback
- helm uninstall
--debug -> enable verbose output


### Helm Components
- Charts: 
- - Charts are colleciton of files.  They contain all the instructions that Helm needs to know to be able to create the collection of objects that we need in our k8s cluster.

- - - - templates directory
- - - - values.yaml
- - - - Chart.yaml
- - - - LICENSE
- - - - README.md
- - - - charts directory for Dependency Charts
---
- Values: 
- - Values.yml file is where the configurable values are stored.  Most of the time, this is the only file we have to modify to customize the deployment of the application for our needs.
---


### Helm repository
- artifacthub.io
- Searching for chart `helm search [command]` example `helm search repo wordpress`
- add repo `helm repo add bitnami https://charts.bitnami.com/bitnami`
- `helm search repo wordpress`
- `helm install my-release bitnami/wordpress`


### Helm Customize
- ``` 
    `helm install --set wordpressBlogName="My-Wordpress-App" my-release bitnami/wordpress
                  --set wordpressEmail="john@exmaple.com`
  ```
- ``


### Helm Lifecyclte management
- outdate helm chart `helm install nginx-release binami/nginx --version 7.1.0` (version is for binami/nginx)
- upgrade helm chart `helm upgrade nginx-release binami/nginx`
- to see old and new versions `helm history nginx-release`
- rollback to specific version `helm rollback dazzling-web 3`