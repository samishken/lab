# Image Security

- To pass the docker credentials to the Docker runtime on the worker nodes
        ```
        kubectl create secret docker-registry regcred \
            --docker-server=
            --docker-username=
            --docker-password=
            --docker-email=
        ```
- Create a secret object with the credentials required to access the registry.        
        ```
        kubectl create secret docker-registry private-reg-cred \
            --docker-server=myprivateregistry.com:5000 \
            --docker-username=dock_user \
            --docker-password=dock_password \
            --docker-email=dock_user@myprivateregistry.com
        ```
- Dockerfile (FROM ubuntu, USER 1000)
- - `docker run --user=1001 ubuntu sleep 3600`
- - `docker run --cap-add MAC_ADMIN ubuntu`

