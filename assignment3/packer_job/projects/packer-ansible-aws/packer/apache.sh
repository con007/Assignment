#!/bin/bash

sudo yum install httpd -y
sudo service httpd start
sudo chkconfig httpd on
sudo touch /var/www/html/index.html
sudo chmod 777 /var/www/html/index.html

echo "Hello Packer " > /var/www/html/index.html
