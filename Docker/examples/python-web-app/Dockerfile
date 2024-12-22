FROM ubuntu:alpine

# CD to /app folder
WORKDIR /app

# moved dependencies file (requirements.txt) into the working directory (/app)
COPY requirements.txt /app
COPY devops /app

# install python
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \

# Ensure devops directory exists and set it as the working directory
WORKDIR /app/devops   

# starting command ENTRYPOINT & CMD
# ENTRYPOINT: Executable can not be changed
ENTRYPOINT ["python3"]

# CMD: executable can be configured (changed)
CMD ["manage.py", "runserver", "0.0.0.0:8000"]




