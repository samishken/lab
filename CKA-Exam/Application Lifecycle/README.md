- Rolling Updates and Rollbacks in deployments
- configure applications
- scale applications
- self-healing applications


#### Deployment Strategies:
- Recreate: turn off old version and add new version
- Rolling update: default stratgey. Replace pods one by one

#### Command line Arguments
- Dockerfile (CMD vs ENTRYPOINT)
- command
- args

#### Environment (end) variables
- Environment variables are frequently used to customize app settings and supply required credentials, making your containers more portable across environments. 
- You can set Kubernetes environment variables using the env and envFrom fields in your Pod manifests.
- when we have a lot of pod definition files it will become difficult to manage the envirnment data stored within the query files.  We can manage centrally using Configuration Maps

#### ConfigMaps
- configmaps store configuration data in plain text
- are used to pass configuration data in the form of key value pairs in Kubernetes.
- when the pod is created inject the ConfigMap into the pod 
- Example: if we set app_color variable in our ConfigMap file. we inject it to our pod definition like below.
    
    `
    envForm:
    - configMapRef:
           name: appcolor
    `
    <br>
    `
    volumes:
    - name: app-config-volume
      configMap:
        name: app-config
    `
- `kubectl create configmap app-config --from-literal=APP_COLOR=blue`
- `kubectl get configmaps`
- `kubectl describe configmaps`


#### Secrets
- Secrets are used to store sensitive information where as ConfigMaps store configuration data in plain text
- `kubectl create secret generic NAME [--type=string] [--from-file=[key=]source] [--from-literal=key1=value1] [--dry-run=server|client|none]`
- `kubectl create secret generic \ <br>
        my-app-secret --from-literal=DB_HOST=mysql <br>
                      --from-literal=DB_User=root <br> 
                      ----from-literal=DB_Password=paswrd <br>
    `
- Secret (my-app-secret) <br>
        `
        DB_HOST: mysql <br>
        DB_User: root <br>
        DB_Password: paswrd <br>
        `
- 
