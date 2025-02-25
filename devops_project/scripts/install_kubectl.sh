#!/bin/bash

# Download kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# Install Kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# Verify Kubectl
kubectl version --client