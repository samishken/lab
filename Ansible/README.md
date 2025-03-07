# Ansible
- Ansible is agentless.  We don't need to install software to run it.
- Ansible connection to establish connection with:
    - - Linux servers via - ssh 
    - - windows servers via - powershell remoting (WinRM)
---
### Ansible Configuration Files
- Default location of Ansible Configuration file -> `/etc/ansible/ansible.cfg`
- when using custom Ansible playbooks for different projects, we add the configuration file in each project direcotry. If we don't add the configuration file in the projects then, it'll use the default configuration file.
- configuration file is separated into different the below sections
- - [default]
- - [inventory]
- - [privilege_escalation]
- - [paramiko_connection]
- - [ssh_connection]
- - [persistent_connection]
- - [colors]


- JSON vs YAML
- YAML (Dictionaries are unordered collection, List are ordered collection)
    - JSON
        ```
        {
            Servers: [
                {
                    name: Server1,
                    owner: John,
                    created: 12232012,
                    status: active
                }
            ]
        }
        ```
    - YAML (Key Value Pair)
        ```
        Servers:
            - name: Server1
              owner: John
              created: 12232012
              status: active
        ```
        - - Array/List
                ```
                Fruits:
                - Ornage
                - Apple
                - Banana
                ```
                ```
                Vegetables:
                - Carrot
                - Cauliflower
                - Tomato
                ```
        - - Dictionary/Map
                ```
                Banana:
                    Calories: 105
                    Fat: 0.4g
                    Carbs: 27 g
                ```
                ```
                Grapes:
                    Calories: 62
                    Fat: 0.3g
                    Carbs: 16 g
                ```

In this lab exercise you will use below hosts. Please note down some details about these hosts as given below :

student-node :- This host will act as an Ansible master node where you will create playbooks, inventory, roles etc and you will be running your playbooks from this host itself.

node01 :- This host will act as an Ansible client/remote host where you will setup/install some stuff using Ansible playbooks. Below are the SSH credentials for this host:
User: bob
Password: caleston123

node02 :- This host will also act as an Ansible client/remote host where you will setup/install some stuff using Ansible playbooks. Below are the SSH credentials for this host:
User: bob
Password: caleston123

### Inventory
- /etc/ansible/hosts
- Inventory file stores information about target systems.
- Inventory file is in INI-like format `server1.compan-name.com`
- define groups:[web_server]
- Add "alias": example - web1 & db1 are alias'
    - - web1 ansible_host=server1.company-name.com
    - - db1 ansible_host=server4.company-name.com
- - `ansible_host`=server1.company-name.com
- - Ansible Host: is an inventory parameter used to specify the FQDN or IP Address of a server.
- - - - ansible_port is set to port 22 by default
- - - - ansible_connection: inventory parameters can be used to establish a local connection instead of ssh in Ansible.  Windows parameter used "winrm" to connect to windos server. "ss" for linux.

# Ini format
[webservers:children]
webservers_us
webservers_eu

[webservers_us]
server1_us.com ansible_host=192.168.8.101
server2_us.com ansible_host=192.168.8.102

[webservers_eu]
server1_eu.com ansible_host=192.168.8.103
server2_eu.com ansible_host=192.168.8.104

# YAML format
all:
  children:
    webservers:
      children:
        webservers_us:
          hosts:
            server1_us.com:
              ansible_host=192.168.8.101
            server2_us.com:
              ansible_host=192.168.8.102
        webservers_eu:
          hosts:
            server1_eu.com:
              ansible_host=192.12.0.103
            server2_eu.com:
              ansible_host=192.12.0.104
\\
# Note: For Linux based hosts, use ansible_ssh_pass parameter and for Windows based hosts, use ansible_password parameter.  Inventory file
# db servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Dbp@ss123!
# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

---------------------------------------------------------------------------
|  Alias |        HOST         | Connection | User          | Password     | 
---------------------------------------------------------------------------
|  web1  | server1.company.com |    ssh     | root          | Password123! |
---------------------------------------------------------------------------
|  web2  | server2.company.com |    ssh     | root          | Password123! |
---------------------------------------------------------------------------
|  web3  | server3.company.com |    ssh     | root          | Password123! |
---------------------------------------------------------------------------
|  db1   | server4.company.com |    winrm   | administrator | Dbp@ss123!   |
---------------------------------------------------------------------------



### Variables

- "Jinja2 templating:  '{{ snmp_port}}'
- Stores information that varies with each host
- host name, usernames
- In palybook, we use  "vars" and key value
- Variable types:
- - String variables: sequences of characters
- - Number variables: hold integers or floating values.
- - Boolean variables: true/false in conditional statement
- - List variables: hold an ordered collection of values.
- - Dictionary variables: hold key value pairs.  name = "adam"

- Registering Variables & Varaible Precedence
- - [web_servers;vars]  dns_server=10.5.5.3
- Extra vars: highest priorit than Play vars, Host vars, Group vars
- - - - Play vars has higher power than Host var, Group vars
- - - - - - Host variable has more power than Group variable

---
(Register Output Scope)
- name: Check /etc/hosts file
  hosts: all
  tasks:
  - shell:  cat /etc/hosts
    register: result <--> (returns resutls)
  - debug:
      var: result  <--> uses the retuned results

- ansible_facts: gather information about the target server (hosts) that are on the playbook only.
- gathering: by default is set to implicit


### Playbooks
- set of instruction (play) to run Ansible
- Task: single action to be performed
- hosts: 
- tasks:
- Verify Ansible Playbook: checking errors before deploying to systems & causing big mistakes.
- - - - check mode: "dry run" ansible runs without making any changes
- - - - - - - - - run "ansible-playbook filename.yml --check"
- - - - diff mode: show what changes a play book makes
- - - - - - - - - run "ansible-playbook filename.yml --diff"
- - - - - - - - - run "ansible-playbook filename.yml --check --diff"
- - - - Syntax Check: Ensures playbook syntax is error-free
- - - - - - - - - run "ansible-playbook filename.yml --syntax-check"
- Ansible Lint - gives us issues with our yaml code
- - - - "ansible-lint filename.yml"
---
- Conditionals statement: when a condition is true -> run
- - "when" a condtion "==" another condition -> run
- - `when item.required == true`
- - `ansible_os_family` Ansible built-in variable populates the flavour of the operating system

---
- LOOPS - there are many **With_** (with_items, with_file, with_url)
        ```
        tasks:
        - user: name='{{ item }}' state=present
            loop:   (or with_items:)
            - joe
            - george
            - ravi
            - mani
            - kiran
        ```

        ```
        tasks:
        - user: name='{{ item.name }}' uid='{{ item.uid }}'state=present
            loop:  (or with_items:)
            - name: joe
                uid: 1010
            - george
                uid: 1011
            - name: ravi
                uid: 1012
            - name: mani
                uid: 1013
            - name: kiran
                uid: 1014
        ```




### Ansible Modules
### Ansible Handlers, Roles, Collection
### Ansible Templates