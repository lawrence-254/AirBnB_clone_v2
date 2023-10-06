#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

#update linux environment
sudo apt-get update
#install nginx if it is not installed
sudo apt-get install -y nginx
#make required directory if they are non existence
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
#create fake html file
sudo sh -c 'echo "simple content to test Nginx!" > /data/web_static/releases/test/index.html'
if [ -e "/data/web_static/current" ]
then
	sudo rm /data/web_static/current
fi
#link two files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#change ownership
chown -R ubuntu:ubuntu /data/
if ! grep -q "location localhost/hbnb_static {" /etc/nginx/sites-available/default; then
	sed -i "/error_page 404 \/404.html;/a \\\n\tlocation /hbnb_static { \
		\n\t\talias /data/web_static/current/; \
		\n\t\tautoindex off; \
		\n\t}" /etc/nginx/sites-available/default
fi
sudo service nginx restart
