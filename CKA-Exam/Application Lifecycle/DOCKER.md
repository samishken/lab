# Commands and Arguments

- Containers are not meant to host operating system.
- Containers are there to run a specific task or process such as to host an instance of a webserver

`docker run ubuntu`
`docker ps` -> we can't see the above container running because conatainer is not meant to host OS.
`docker ps -a` -> can only be seen


### CMD vs. ENTRYPOINT in Docker: Clearing the Confusion

- When working with Docker, CMD and ENTRYPOINT are often used interchangeably, but they serve different purposes in defining how a container starts. 
- We can combine ENTRYPOINT with CMD to specify default arguments for that entry point.
- when we combine the two CMD overrides ENTRYPOINT
- Entrypoint: can not be changed. Executable can not be changed
- CMD: configurable

##### CMD
- CMD in dockerfile defines the program that can be run when the program starts
- Example `CMD ["nginx]`
- provides the default command and arguments for the container when no other command is specified during container runtime. 
- It's used as fallback or default value for the command to run inside the container.

#### ENTRYPOINT
- is a command instruction that can help us specify the program that will be run when the container starts and whatever we specify on the command line.
- sets the main command to run when the container starts. 
- It is more rigid and defines the core process for the container, making it non-optional. 

- If Dockerfile has an ENTRYPOINT as well as CMD instruction specified, then ENTRYPOINT is the command that is run at startup, and the CMD is the default parameter passed to the command.
- With the args option in the pod definition file we override the CMD instruction in the Dockerfile.

`
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper-pod
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu-sleeper
    command: ["sleep"]  # Entrypoint in dockerfile
    args: ["10"]  # CMD field in dockerfile
`

##### Misconception: Many think CMD and ENTRYPOINT do the same thing. However, ENTRYPOINT defines the main command, while CMD provides default arguments or can be overridden.

##### Key Takeaway: Use ENTRYPOINT to define the core process of the container and CMD to specify default arguments or an override option.