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