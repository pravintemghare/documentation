## Loops
- Use loops for a repeatative tasks
- {{ item }} is used when going through the loop

Sample:
    - 
        name: Play
        hosts: localhost
        tasks:
            - user: name = '{{ item.name }}' state=present uid='{{ item.uid }}' 
              loop:
                - name: user1
                  udi: 1001
                - name: user2
                  uid: 1002

with_* -- look up plugins