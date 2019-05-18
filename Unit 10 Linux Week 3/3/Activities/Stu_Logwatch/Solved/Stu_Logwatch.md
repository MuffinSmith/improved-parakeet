## Sysadmin Essentials: Monitoring Log Files 

--------

## Solutions: Monitoring Cron Logs with logwatch

------


* First display the `man page` for `logwatch and review the options.

    `man logwatch`

**Exercise 1:** 

* Manually send a digest for **today's cron activity** to `mylogwatch.txt`.

    `logwatch --service cron --filename logwatchcron.txt --range today`

* View the activity in the `mylogwatch.txt` file.

    `nano mylogwatch.txt`
    
**Exercise 2:**

* Use the digest [SampleDigest](SampleDigest.pdf) to analyze system activity or errors. 

    * Packages were upgraded.

    * Cron stats.

    * Kernel errors.

    * Disk space stats.
