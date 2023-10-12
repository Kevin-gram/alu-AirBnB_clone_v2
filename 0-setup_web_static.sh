#!/usr/bin/env bash

# Update packages and install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create directory structure
sudo mkdir -p /data/web_static/{shared,releases/test}
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set permissions
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx
sudo sed -i '/# pass the PHP/i location /hbnb_static {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

