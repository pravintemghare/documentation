#
- Ansible can work with multiple infra at the same time
- SSH connectivity is the only need to work with ansible
- Inventory file /etc/ansible/hosts

Sample:
[webserver]  -- Group
webserver1.example.com
webserver2.example.com

web ansible_host=server1.example.com ansible_connection=ssh/winrm ansible_port=22/5986 ansible_user=root/administrator ansible_ssh_pass=Password