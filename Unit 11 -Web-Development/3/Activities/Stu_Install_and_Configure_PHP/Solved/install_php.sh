#!/usr/bin/env bash

# Install
sudo apt-get install php libapache2-mod-php php-mysql

# Edit the DirectoryIndex line so `index.php` is before `index.html`
sudo nano /etc/apache2/mods-enabled/dir.conf

# Create a test file w/ echo
sudo echo '<?php phpinfo(); ?>' > /var/www/html/info.php

# Navigate to: `http://localhost/info.php`

# Remove the test file for security
sudo rm /var/www/html/info.php
