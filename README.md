# ansible-example roles
Collection of Ansible examples
## users
Used when you want to be able to quickly build up a set of users with ssh keys. I will put a default user in the playbook, and allow fact merging to add in additional users per environment.
Example playbook: users.yml
## etc_hosts
Example inventory:
```
[jenkins]
192.168.1.2 hostname="jenkins-master1"

[sonar]
192.168.1.3 hostname="sonar1"

[nexus]
192.168.1.4 hostname="nexus1"

[subdomain:children]
jenkins
sonar
nexus

[subdomain:vars]
domain="devops.local"
```

Used when you don't have have real networking and you need to abuse /etc/hosts to fake hostnames. It will combine ips from the inventory with the fact dictionary "etc_hosts_aliases"
Example playbook: etc_hosts.yml

## security_update

Example playbook: security_update.yml
