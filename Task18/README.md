# Task 15
**Tested on RHEL8.3**

To run :
1. Download wordpress file from this site https://wordpress.org/
or use this in command line

    `wget https://wordpress.org/latest.tar.gz`
2.  Configure Repository for EPEL and REMI using root user  

    * `yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm`  
    * `sudo dnf -y install https://rpms.remirepo.net/enterprise/remi-release-8.rpm`
3. Install software needed to run Wordpress

   | Software Name    |    Command |
   |-------------------|--------------------------|
   | php:nemi-7.4   |    `yum install php:remi-7.4`|
   |php-mysqlnd|`yum install php-mysqlnd`|
   |mysql| `yum install mysql`|
   |php| `yum install php`|
   
4. Stop firewall 
* `setenforce 0`
5. Make the extracted folder writable
* `chmod 777 <filename>`
6. Now you can browse 
