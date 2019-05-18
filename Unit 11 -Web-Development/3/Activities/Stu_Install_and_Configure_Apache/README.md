# Installing Apache

- Install Apache using `apt`.
  - The package is named `apache2`.

- The next step is to update the Apache configuration with a `ServerName`. For our purposes, the `ServerName` should be your computer's public IP address. 
  - Find your public IP address using curl to send a GET request to `http://icanhazip.com`.
  - Add the line: `ServerName <Your Public IP Address>`to the end of the file `/etc/apache2/mods-enabled/dir.conf`. 

- Restart Apache, and ensure the server starts on boot.
  - **Hint**: Use `sudo service apache2 restart` to restart. Figure out how to enable on startup yourself.

<!--- Next, update your UFW rules to use the `Apache Full` security profile.-->

- Use cURL to send a GET request to `http://localhost/index.html`. You should see HTML!
