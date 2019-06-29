## Scheduling Backups

### Scenario

In this activity, you will resume the role of a Network Administrator. Although we cannot mitigate all attacks, we can recover from them. If a system is failing or has malware, often the best thing to do is unplug and restore it with the latest backup. You will now be using cron to create automated backups so you won't have to (matrix).


### Instructions
- Write a cronjob that creates a bzipped backup of your root directory every sunday at midnight. It should always save to `/var/backups/backup.tar`.

- Write a cronjob to _update_ the backup of the `/home` directory in the `backup every day at midnight.

- In practice, the `--update` option is not used to create backups. Read this article and the link therein for more information as to why: <https://www.gnu.org/software/tar/manual/html_node/how-to-update.html>

- What _is_ the correct way to create frequently updated backups? 
  - **Hint**: Recall your Linux 3 homework.