# Installing PHP

- Install the following packages with apt: `php libapache2-mod-php php-mysql`

- Update Apache to load `index.php` instead of `index.html`.
  - Edit the file: `/etc/apache2/mods-enabled/dir.conf`
  - Find the line that starts with: `DirectoryIndex`
  - Move `index.php` _before_ `index.html`.
  - Save the file (in nano, press `Ctrl + X`).

- Create a file to test your PHP installation in `/var/www/html/info.php`. It should contain the line: `<?php phpinfo(); ?>`

- Open a browser and navigate to `http://localhost/info.php`.

- Finally, remove `/var/www/html/info.php`.
