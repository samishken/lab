# Ansible Modules

Ansible modules are discrete units of code that perform specific tasks in an Ansible playbook. They enable automation of system configurations, deployments, and other operations.

## Types of Ansible Modules

Ansible provides various modules categorized as follows:

- **Core Modules**: Maintained by the Ansible team and included by default.
- **Community Modules**: Contributed by the Ansible community.
- **Custom Modules**: User-defined modules for specific use cases.

## Commonly Used Ansible Modules

### 1. Package Management Modules
These modules manage software installation and updates.

- `yum` - Manages RPM packages (RHEL/CentOS).
- `apt` - Manages APT packages (Debian/Ubuntu).
- `dnf` - Manages DNF-based package installations.
- `pip` - Manages Python packages.

Example:
```yaml
- name: Install Nginx
  hosts: all
  tasks:
    - name: Install Nginx using apt
      ansible.builtin.apt:
        name: nginx
        state: present
```

### 2. Service Management Modules
These modules manage system services.

- `service` - Controls services (start, stop, restart).
- `systemd` - Manages systemd services.
- `sysvinit` - Manages SysVinit services.

Example:
```yaml
- name: Start and enable Nginx service
  hosts: all
  tasks:
    - name: Ensure Nginx is running
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: yes
```

### 3. Firewall Management Modules
These modules configure firewalls.

- `ufw` - Manages UFW firewall (Ubuntu).
- `firewalld` - Manages firewalld (RHEL/CentOS).
- `iptables` - Manages iptables rules.

Example:
```yaml
- name: Allow HTTP through UFW
  hosts: all
  tasks:
    - name: Open port 80
      ansible.builtin.ufw:
        rule: allow
        port: '80'
        proto: tcp
```

### 4. File Management Modules
These modules handle file attributes and contents.

- `file` - Manages file permissions and ownership.
- `copy` - Copies files to remote systems.
- `template` - Renders Jinja2 templates.
- `lineinfile` - Ensures a specific line exists in a file.
- `replace` - Replaces text in a file.

Example:
```yaml
- name: Ensure a configuration setting is present
  hosts: all
  tasks:
    - name: Add a line to a config file
      ansible.builtin.lineinfile:
        path: /etc/example.conf
        line: 'setting=true'
        create: yes
```

### 5. Archiving Modules
These modules handle compression and extraction.

- `archive` - Creates compressed archives.
- `unarchive` - Extracts compressed archives.

Example:
```yaml
- name: Compress a directory
  hosts: all
  tasks:
    - name: Create a tarball of /var/logs
      ansible.builtin.archive:
        path: /var/logs
        dest: /backup/logs.tar.gz
```

### 6. Cron Job Management Modules
These modules manage scheduled tasks.

- `cron` - Manages cron jobs.
- `at` - Schedules one-time tasks.

Example:
```yaml
- name: Schedule a cron job
  hosts: all
  tasks:
    - name: Run a script every day at midnight
      ansible.builtin.cron:
        name: "Daily backup"
        minute: "0"
        hour: "0"
        job: "/usr/local/bin/backup.sh"
```

## Using a Module in a Playbook

Example of using the `user` module:

```yaml
- name: Create a user
  hosts: all
  tasks:
    - name: Add user 'john'
      ansible.builtin.user:
        name: john
        state: present
```

For a full list of modules, check the [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/list_of_modules.html).

