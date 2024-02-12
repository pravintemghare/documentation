## Variables
- Store information that varies with each host

#### To create variable
- We can create variables in playbook or in a seperate file

Sample:
    -
        name: Playname
        hosts: localhost
        vars:
            dns_server: 8.8.8.8   -- define variable
        
        tasks:
            - lineinfile:
                path: /etc/resolv.conf
                line: 'name server {{ dns_server }}'  -- refer the variable. if the variable is in between sentence single quotes not required.
                line: name server {{ dns_server }} done
                line: '{{ dns_server }}'