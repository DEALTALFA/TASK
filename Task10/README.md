# Task 10
Note: tested on REDHAT 8.3 only

How To Run:
1. Add the Manages Node user to sudoers file .Just from the bottom of the file find :

``root ALL=(ALL)    ALL``

below it add

``<user> ALL=(ALL)  NOPASSWD: ALL``

2. In the yml file change the hosts accordingly to your choice
3. In the [inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html) add ansible_become=true and ansible_become_method=sudo
       or 
   You can make changes in configuration file [click here](https://docs.ansible.com/ansible/2.3/become.html)
4. Run the playbook
