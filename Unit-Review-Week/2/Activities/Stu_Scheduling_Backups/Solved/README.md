# Scheduling Backups

## Instructions
- Write a cronjob that creates a bzipped backup of your root directory every sunday at midnight. It should always save to `/var/backups/backup.tar`.
  > **Solution**: `0 0 0 0 0 tar cvf / /var/backups/backup.tar` or `@weekly tar cvf / var/backups/backup.tar`.

- Write a cronjob to _update_ the backup of the `/home` directory in the `backup every day at midnight.
  > **Solution**: `@daily tar --update /var/backups/backup.tar /home`

- In practice, the `--update` option is not used to create backups. Read this article and the link therein for more information as to why: <https://www.gnu.org/software/tar/manual/html_node/how-to-update.html>

- What _is_ the correct way to create frequently updated backups? 
  - **Hint**: Recall your Linux 3 homework.
  > **Solution**: `--update` isn't used to create backups because it doesn't update directory content entries, and because it increases the size of the archive each time it's run. This is why it's not used to create backups. Instead, incremental backups should be used.