#!/bin/bash
# Print the hostname of all managed nodes in the inventory file ~/playbooks/inventory 
ansible all -a "hostname" -i inventory

# Using copy module copy the /etc/resolv.conf file from ansible controller to /tmp/resolv.conf on node00 host. Use the inventory file ~/playbooks/inventory. 
ansible node00 -m copy -a "src=/etc/resolv.conf dest=/tmp/resolv.conf" -i inventory

# Run an ad-hoc command to print the uptime 


# Set ANSIBLE_GATHERING to explicit
export ANSIBLE_GATHERING=explicit
# print 'uptime'
ansible all -m command -a "uptime" -i inventory

# cat the file /etc/redhat-release on all managed nodes
ansible-playbook -i inventory playbook.yml -vv
 