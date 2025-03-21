# Ansible configuration files
# Default Location `/etc/ansible/ansible.cfg`

Custom location
- before running the ansible playbook, we can specify the location to this configuration file through environment variable, ansible_config and set it to the paths to the new config file.
- Example: `$ANSIBLE_CONFIG=/opt/ansible-web.cfg ansible-playbook playbook.yml`

- Order of 

- `ansible-config list` # list alll configurations
- `ansible-config view` # shows the current config file
- `ansible-config dump` # shows the current settings
- `$ export ANSIBLE_GATHERING=explicit`
- `$ ansible-config dump | grep GATHERING`  # DEFAULT_GATHERING(env: ANSIBLE_GATHERING) = explicit