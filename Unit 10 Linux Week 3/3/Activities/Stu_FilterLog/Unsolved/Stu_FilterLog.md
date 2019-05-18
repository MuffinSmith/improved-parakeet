## Sysadmin Essentials: Monitoring Log Files 

--------

## Instructions 

------

## A Better Way to Administer Log Files

**Instructions**

In these exercises, you use **journalctl** to filter logs for the `cron` service using combinations of options and keywords.  

* Open a terminal window on the Virtual Machine.

* View the **man page** for `journalctl`

**Exercise 1:**

* Obtain the date / time on the system and view the log for `cron` up to that time.

**Exercse 2:**

* View the log for `cron` without `metadata` for the `last 20 minutes`. 

**Exercise 3:**

* View the log for `cron` so that the latest enteries are display first.

**Exercise 4:**

* Review and analyze the results from `journalctl` (for the system as a whole) to determine what activities are frequently logged?

* **Challenge:** 

* Export the journal log for `cron` to `exportlog.txt`. This seralizes the data for backups or network transfer.
