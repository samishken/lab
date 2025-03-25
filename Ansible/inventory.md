### Sample inventory
- web1 ansible_host=172.20.1.100 ansible_user=root ansible_password=Passw0rd
- web1 ansible_host=172.20.1.100 ansible_user=ansible ansible_ssh_private_key_file=~/.ssh/ansible

#### Setting up Groups, Ip address, Username and Password.  Add database infor and web info
[db_servers]
lamp-db ansible_host=172.20.1.101 ansible_user=maria mysqlservice=mysqld mysql_port=3306 dbname=ecomdb dbuser=ecomuser dbpassword=ecompassword

[web_servers]
lamp-web ansible_host=172.20.1.100 ansible_user=john httpd_port=80 repository=https://github.com/kodekloudhub/learning-app-ecommerce.git


### Add ssh from controller to servers
- ssh-copy-id -i /home/thor/.ssh/john  john@lamp-web
- ssh-copy-id -i /home/thor/.ssh/maria  maria@lamp-db

### Update the inventory file to use the newly created private keys for the respective hosts 
[db_servers]
lamp-db ansible_host=172.20.1.101 ansible_ssh_private_key_file=/home/thor/.ssh/maria ansible_user=maria mysqlservice=mysqld mysql_port=3306 dbname=ecomdb dbuser=ecomuser dbpassword=ecompassword

[web_servers]
lamp-web ansible_host=172.20.1.100 ansible_ssh_private_key_file=/home/thor/.ssh/john ansible_user=john httpd_port=80 repository=https://github.com/kodekloudhub/learning-app-ecommerce.git

