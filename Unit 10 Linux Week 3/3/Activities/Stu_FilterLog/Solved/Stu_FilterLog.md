## Sysadmin Essentials: Monitoring Log Files

--------

 ## Solutions: A Better Way to Filter Log Files

------

* View the **man page** for `journalctl`.

    * `man journalctl`

**Exercise 1:**    

* Obtain the date / time on the system and view the log for `cron` up to that time.

    * `date`

    * `journalctl  --until <year-mon-day> <hr:min:sec> -u cron`

**Exercise 2:**    

* View the log for `cron` without `metadata` for the `last 20 minutes`.

    * `journalctl -o cat --since -20m -u cron`

**Exercise 3:**    

* View the log for `cron` so that the newest enteries are display first.

    * `journalctl -r -u cron`

**Exercise 4:**

* Review and analyze the results from `journalctl` (for the system as a whole) to determine what activities are frequently logged?

    * `journalctl | less`


* **Challenge**

* Export the journal log for `cron` to `exportlog.txt`. This seralizes the data for backups or network transfer.

    * `journalctl -o export -u cron > exportlog.txt`
