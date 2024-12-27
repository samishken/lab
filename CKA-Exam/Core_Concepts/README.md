### Here’s a tip!

As you might have seen already, creating and editing YAML files is a bit difficult, especially in the CLI. <br>
During the exam, you might find it difficult to copy and paste YAML files from the browser to the terminal. <br>
Using the `kubectl run` command can help in generating a YAML template. <br>
And sometimes, you can even get away with just the `kubectl run` command without having to create a YAML file at all.  <br>
For example, if you were asked to create a pod or deployment with a specific name and image, you can simply run the `kubectl run` command. <br>

Use the below set of commands and try the previous practice tests again, but this time, <br> 
try to use the below commands instead of YAML files. Try to use these as much as you can going forward in all exercises. <br>

Reference (Bookmark this page for the exam. It will be very handy):<br>

https://kubernetes.io/docs/reference/kubectl/conventions/ <br> 

##### Create an NGINX Pod <br>
`kubectl run nginx --image=nginx` <br>

##### Generate POD Manifest YAML file (-o yaml). Don’t create it(–dry-run) <br>
`kubectl run nginx --image=nginx --dry-run=client -o yaml` <br>

##### Create a deployment<br>
`kubectl create deployment --image=nginx nginx` <br>

##### Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) <br>
`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml` <br>

##### Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file. <br>
`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml` <br>

##### Make necessary changes to the file (for example, adding more replicas) and then create the deployment. <br>
`kubectl create -f nginx-deployment.yaml` <br>
OR <br>

##### In k8s version 1.19+, we can specify the –replicas option to create a deployment with 4 replicas. <br>
`kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-d` <br>


While you would be working mostly the declarative way – using definition files, imperative commands can help in getting one-time tasks done quickly, as well as generate a definition template easily. <br>
This would help save a considerable amount of time during your exams. Before we begin, familiarize yourself with the two options that can come in handy while working with the below commands: <br>

`--dry-run` By default as soon as the command is run, the resource will be created. <br>
If you simply want to test your command, use the --dry-run=client option. This will not create the resource; instead, it tells you whether the resource can be created and if your command is right. <br>

`-o yaml` This will output the resource definition in YAML format on the screen. <br>

Use the above two in combination to generate a resource definition file quickly that you can then modify and create resources as required instead of creating the files from scratch. <br>

### POD
##### Create an NGINX Pod
`kubectl run nginx --image=nginx`

##### Generate POD Manifest YAML file (-o yaml). Don’t create it(–dry-run)
`kubectl run nginx --image=nginx --dry-run=client -o yaml`

### Deployment
##### Create a deployment
`kubectl create deployment --image=nginx nginx`

##### Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run)
`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml`

##### Generate Deployment with 4 Replicas
`kubectl create deployment nginx --image=nginx --replicas=4`

##### You can also scale a deployment using the
`kubectl scale` command.

`kubectl scale deployment nginx--replicas=4`

##### Another way to do this is to save the YAML definition to a file and modify
`kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml`

You can then update the YAML file with the replicas or any other field before creating the deployment.

### Service

##### Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379

```kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml```
##### (This will automatically use the pod’s labels as selectors)

Or

`kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml`
##### (This will not use the pods labels as selectors, instead, it will assume selectors as app=redis.

You cannot pass in selectors as an option.

So, it does not work very well if your pod has a different label set. So, generate the file and modify the selectors before creating the service)

Create a Service named nginx of type NodePort to expose pod nginx’s port 80 on port 30080 on the nodes:
`kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml`

##### (This will automatically use the pod’s labels as selectors, but you cannot specify the node port. You have to generate a definition file and then add the node port manually before creating the service with the pod.)
Or

`kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml`

##### (This will not use the pod labels as selectors.)
##### Both the above commands have their own challenges. While one of them cannot accept a selector, the other cannot accept a node port. I would recommend going with the
`kubectl expose`command. If you need to specify a node port, generate a definition file using the same command and manually input the nodeport before creating the service.

##### Reference:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands

https://kubernetes.io/docs/reference/kubectl/conventions/