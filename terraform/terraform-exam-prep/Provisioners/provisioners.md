# Terraform Provisioners​
- `Terraform Provisioners` install software, edit files, and provision machines created with Terraform​
- Terraform allows you to work with two different provisioners:​

### cloud-init

Cloud-Init is an industry-standard for cross-platform cloud instance initializations. When you launch a VM on a Cloud Service Provider (CSP) you’ll provide a YAML or Bash script.​

### Packer

Packer is an automated image-builder service. You provide a configuration file to create and provision the machine image and the image is delivered to a repository for use.​

---
## Local-exec​
- Local-exec allows you to execute `local commands` after a resource is provisioned.​
- local machine like laptops

            ```
            provisioner "local-exec" {
                command = "echo ${self.private_ip} >> private_ips.txt
                interpreter = ["Powershell", "-Command"]
                environment = {
                    KEY = "SSSSTTTTXXVVVVXXXYYYZZZ"
                    VALUE = "AFASDJFLADSFADFASFDFJLDSFJ"
                }
            }
            ```
- Command: the command we want to execute
- Working-dir: where the command will be executed
- interpreter: entry point for a command. 
- Environment: key and value pair of environment 
---
## Remote-exec
- `Remote-exec` allows you to execute commands on a target resource after a resource is provisioned.​
- Local Machine executing Terraform​ → remote-exec → Provisioned VM (resource) executing provided commands script
- `remote-exec` allows you to execute `commands on a target resource` after a resource is provisioned.
- `remote-exec` is used for running commands on a running instance after it has been created.​

```
provisioner "remote-ext"{
    inline = [
        "puppet apply",
        "consul join ${aws_instance.web.private_ip}",
    ]
    scripts = [
        "./setup-user.sh",
        "/home/name/Desktop/bootstrap"
    ]
}
```
## File​ 
- `file provisioner` is used to copy files or directories from our local machine to the newly created resource​
- - Source – the local file we want to upload to the remote machine​​
- - Content – a file or a folder​
- - Destination – where you want to upload the file on the remote machine​

        ```
        resource "aws_instance" "web" {
        # ...

        # Copies the myapp.conf file to /etc/myapp.conf
        provisioner "file" {
            source      = "conf/myapp.conf"
            destination = "/etc/myapp.conf"
        }

        # Copies the string in content into /tmp/file.log
        provisioner "file" {
            content     = "ami used: ${self.ami}"
            destination = "/tmp/file.log"
        }

        # Copies the configs.d folder to /etc/configs.d
        provisioner "file" {
            source      = "conf/configs.d"
            destination = "/etc"
        }

        # Copies all files and folders in apps/app1 to D:/IIS/webapp1
        provisioner "file" {
            source      = "apps/app1/"
            destination = "D:/IIS/webapp1"
            }
        }
        ```
---
## Connection​
- A connection block tells a provisioner or resource how to establish a connection​
- You can connect via `SSH​`

```
        # connects via ssh
        provisioner "file" {
            source      = "apps/app1/"
            destination = "D:/IIS/webapp1"
            connection {
                type     = "ssh"
                user     = "ubuntu"
                password = "${var.ubuntu_password}"
                host     = "${var.host}"
            }    
        }
```
---
## Null Resources
- `null_resource` is a placeholder for resources that have no specific association to a provider resources.

## Terraform Data
- Similar to `null_resources` but does not require or the configuration of a provider.​

        ```
        resource "aws_instance" "cluster" {
        count         = 3
        ami           = "ami-0dcc1e21636832c5d"
        instance_type = "m5.large"

        # ...
        }

        # The primary use-case for the null resource is as a do-nothing container
        # for arbitrary actions taken by a provisioner.
        #
        # In this example, three EC2 instances are created and then a
        # null_resource instance is used to gather data about all three
        # and execute a single action that affects them all. Due to the triggers
        # map, the null_resource will be replaced each time the instance ids
        # change, and thus the remote-exec provisioner will be re-run.
        resource "null_resource" "cluster" {
        # Changes to any instance of the cluster requires re-provisioning
        triggers = {
            cluster_instance_ids = join(",", aws_instance.cluster[*].id)
        }

        # Bootstrap script can run on any instance of the cluster
        # So we just choose the first in this case
        connection {
            host = element(aws_instance.cluster[*].public_ip, 0)
        }

        provisioner "remote-exec" {
            # Bootstrap script called with private_ip of each node in the cluster
            inline = [
            "bootstrap-cluster.sh ${join(" ",
            aws_instance.cluster[*].private_ip)}",
            ]
        }
        }

        ```
---
