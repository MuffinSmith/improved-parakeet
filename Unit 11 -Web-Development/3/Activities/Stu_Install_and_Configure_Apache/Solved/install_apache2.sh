#!/usr/bin/env bash

# Install
sudo apt-get install apache2

# Get your public IP address
curl http://icanhazip.com

# Add a global ServerName to Apache configuration to suppress warnings
sudo nano /etc/apache2/apache2.conf
ServerName <ipaddress>

# Verify configuration
sudo apache2ctl configtest

# Ensure server is running with new configuration
sudo service apache2 restart

# Launch server on boot
sudo update-rc.d apache2 defaults

# Update Firewall
sudo ufw list
sudo ufw allow 'Apache Full'
sudo ufw status
sudo ufw enable

# Test web server
curl localhost
