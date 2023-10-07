#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

#update linux environment
sudo apt-get update
#install nginx if it is not installed
sudo apt-get install -y nginx
#make required directory if they are non existence
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_alias="location /hbnb_static/ {\n    alias /data/web_static/current/;\n}"
if ! grep -q "$config_alias" "$config_file"; then
    sed -i "/server_name _;/a $config_alias" "$config_file"
fi

# Restart Nginx
service nginx restart

exit 0
