# Ansible configuration files
# Default Location `/etc/ansible/ansible.cfg`

Custom location
- before running the ansible playbook, we can specify the location to this configuration file through environment variable, ansible_config and set it to the paths to the new config file.
- Example: `$ANSIBLE_CONFIG=/opt/ansible-web.cfg ansible-playbook playbook.yml`
- Run the ansible command to gather facts of the localhost and save the output in /tmp/ansible_facts.txt file. `ansible -m setup localhost > /tmp/ansible_facts.txt`
- 
- Execute an ad-hoc command to perform a ping connectivity test for the localhost and save the output in /tmp/ansible_ping.txt file.  `ansible -m ping localhost > /tmp/ansible_ping.txt`
-
- Run an adhoc command to perform a ping connectivity to all hosts in the /home/thor/playbooks/inventory file and save the output in /tmp/ansible_all.txt file.  `ANSIBLE_HOST_KEY_CHECKING=False ansible -m ping -i /home/thor/playbooks/inventory all > /tmp/ansible_all.txt`
-
- Run an adhoc command to run a command on host web1 to print the date and save the output in /tmp/ansible_date.txt file on the ansible controller. `ansible web1 -m shell -a "date" -o | tee /tmp/ansible_date.txt`


- Order of 

- `ansible-config list` # list alll configurations
- `ansible-config view` # shows the current config file
- `ansible-config dump` # shows the current settings
- `$ export ANSIBLE_GATHERING=explicit`
- `$ ansible-config dump | grep GATHERING`  # DEFAULT_GATHERING(env: ANSIBLE_GATHERING) = explicit

--- 
- ssh-keygen -t ed25519 -C "my-work-key" / ssh-keygen -t rsa -f ~/.ssh/ansible
- ssh (cat ~/.ssh/authorized_keys)
- Inventory 
- `web1 ansible_host=172.20.1.100 ansible_user=ansible ansible_ssh_private_key_file=~/.ssh/ansible`

--- 
### Adhoc Commands
-
- Print the hostname of all managed nodes in the inventory file ~/playbooks/inventory `ansible all -a "hostname" -i inventory`
-
- Using copy module copy the /etc/resolv.conf file from ansible controller to /tmp/resolv.conf on node00 host. Use the inventory file ~/playbooks/inventory. `ansible node00 -m copy -a "src=/etc/resolv.conf dest=/tmp/resolv.conf" -i inventory`