FROM ubuntu:alpine

# CD to /app folder
WORKDIR /app

# moved dependencies file (requirements.txt) into the working directory (/app)
COPY requirements.txt /app
COPY devops /app

# Install Python and pip, and install dependencies
RUN apt-get update && \
    apt-get install -y python3-requests python3-pip && \
    pip install --break-system-packages -r requirements.txt && \
    cd devops

# starting command ENTRYPOINT & CMD
# ENTRYPOINT: Executable can not be changed
ENTRYPOINT ["python3"]

# CMD: executable can be configured (changed)
CMD ["manage.py", "runserver", "0.0.0.0:8000"]




