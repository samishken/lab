# Docker notes

- Exposing Ports <br>
    - From the host expose container
    - Example: Nginx by default uses port 80 to access the container
    - If we run `docker run -d --name first-container -p 8080:80 nginx:latest`
    - "-p 8080:80" stands for from the host issue a request to connect via port 8080. The default is port 80
    <br>
    - Format <br>
        - RUN export FORMAT="ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"
        - RUN docker ps --format=$FORMAT
- Docker Volumes
    - Helps us share data between host and container and container <-> container
    - Example mount index.htm from current folder to Nginx "docker run -d --name website -v $(pwd):/usr/share/nginx/html:ro -p 8081:80 nginx:latest"
    - RUN `docker exec -it website bash`
    - RUN `cd /usr/share/nginx/html/`
    - "/usr/share/nginx/html:ro" read-only can not add more files
    - To make it read & write run the following
    - `docker run -d --name website -v $(pwd):/usr/share/nginx/html -p 8081:80 nginx:latest`
    - <br>
    - Share data between containers
    - RUN `docker run -d --name website-copy --volumes-from website -p 8082:80 nginx:latest`

- Dockerfile
    - helps us create custom images
    - Series of steps that define how our images are built
    - `docker build --tag website:alpine .`
    - or `docker build -t website:alpine .`