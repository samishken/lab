# Create custom Helm repo and chart

mkdir -p best-commerce/{payments,shipping}
cd best-commerce
`helm create payments` - creates CHARTS folder (can be ignored), TEMPLATES folder, .helmignore file, Chart.yaml file, values.yaml file
`helm create shipping` - - creates CHARTS folder (can be ignroed), TEMPLATES folder, .helmignore file, Chart.yaml file, values.yaml file
- Outcome
```
├── payments
│   ├── Chart.yaml
│   ├── charts
│   ├── templates
│   │   ├── NOTES.txt
│   │   ├── _helpers.tpl
│   │   ├── deployment.yaml
│   │   ├── hpa.yaml
│   │   ├── ingress.yaml
│   │   ├── service.yaml
│   │   ├── serviceaccount.yaml
│   │   └── tests
│   │       └── test-connection.yaml
│   └── values.yaml
└── shipping
    ├── Chart.yaml
    ├── charts
    ├── templates
    │   ├── NOTES.txt
    │   ├── _helpers.tpl
    │   ├── deployment.yaml
    │   ├── hpa.yaml
    │   ├── ingress.yaml
    │   ├── service.yaml
    │   ├── serviceaccount.yaml
    │   └── tests
    │       └── test-connection.yaml
    └── values.yaml
```
---
- `Chart.yml`: metadata for the chart. Will have information about owner,version, what is the version of application in the chart
- `Values.yml`: used to customize files in Templates folder.
- `Templates` folder: add necessary yaml files for k8s cluster. (Ex. deployment.yaml, hpa,yal, ingress.yml, service.yml, serviceaccount.yml)

### Create helm chart (creates zip file after we run the following. Unzip)
- `helm package payments`
- `helm package shipping`

### Create bundle the charts to -> index.yml
- `helm repo index .`
      
        ```
        apiVersion: v1
        entries:
        payments:
        - apiVersion: v2
            appVersion: 1.0.0
            created: "2025-06-20T16:02:24.533635158-04:00"
            description: A Helm chart for Kubernetes
            digest: b2437c517f5a66912ea6e4afd2f905b9fd2a7621a9dff589a59810a83f3d6f41
            name: payments
            type: application
            urls:
            - payments-0.1.0.tgz
            version: 0.1.0
        shipping:
        - apiVersion: v2
            appVersion: 1.0.0
            created: "2025-06-20T16:02:24.534160389-04:00"
            description: A Helm chart for Kubernetes
            digest: 777d757ee6ed60b3c6019ebdb11dc3f876c788f5601608c64e6d06183f149366
            name: shipping
            type: application
            urls:
            - shipping-0.1.0.tgz
            version: 0.1.0
        generated: "2025-06-20T16:02:24.531945776-04:00"
        ```
#### To install and view values of helm chart.
```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=my-cluster \                  => values for the helm chart
  --set serviceAccount.create=false \                  => values for the helm chart
  --set serviceAccount.name=aws-load-balancer-controller \        => values for the helm chart
  --version 1.13.0   => values for the helm chart
```
- To see values `helm show values eks/aws-load-balancer-controller`