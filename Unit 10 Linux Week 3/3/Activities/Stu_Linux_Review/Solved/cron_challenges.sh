# Run at midnight every Sunday. Sunday can be 0 or 7.
* * * * 7 tar cfvj /var/backups/home.tar.bz2

# Run every day at 5AM
* 5 * * * tar cfvz /var/backups/logs.tar.bz2
