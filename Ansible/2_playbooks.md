## Playbooks
- Playbooks are ansible orchestration language
- Playbooks are set of instruction we define what ansible will do on remote machines

## Playbook
- Playbook are written in yaml
- Play - defines a set of activites to run on the hosts
- Task - an action to be performed on the host
    - execute a command
    - run a script
    - install a package
    - shutdown/restart

`ansible-playbook -i inventory_file playbook.yaml`