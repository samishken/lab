### Helm: The package manager for Kubernetes

# Documentation: https://helm.sh/docs/

# Install Helm
-- # Download the install shell script
- $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
-- # Allow to Run
- chmod 700 get_helm.sh
-- # Install
- $ ./get_helm.sh
-- # Confirm it works
- $ helm version
   

# Helm Notes

- values.yaml file : contains all the default values.  It provides access to values passed into the chart.
- Templates
- helm show values


# Helm upgrade with new custom values
- example: helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack -n our-monitoring --values values.yaml