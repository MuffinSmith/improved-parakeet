# Submission

### Tar
#### Stripping Components
- **Exercise 2**
  - Extract `Movies`: `tar -xf TarDocs.tar --strip-components=1 "TarDocs/Movies"`
  - Extract `Movies/ZOE_0004.mp4`: `tar -xf TarDocs.tar --strip-components=2 "TarDocs/Movies/ZOE_0004.mp4"`

#### Modifying Archives
- **Exercise 1**

  ```bash
  # Insert the solution commands for Exercise 1 below
  tar --concatenate --file=update.tar sample.tar
  tar --list --file=update.tar
  touch test1.txt test2.txt
  tar -rf update.tar test1.txt test2.txt
  tar --list --file=update.tar
  ```

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
  tar -uf update.tar test2.txt
  tar --list --file=update.txt
  ```

- **Exercise 3**

  ```bash
  # Insert the solution commands for Exercise 3 below
  tar --delete --file=update.tar test1.txt 
  tar --list --file=update.tar
  ```

#### Incremental Backups
- **Exercise 1**
  - A **snapshot file** is `A snapshot file is a file containing metadata for what files were changed and what the change was so that you can save storage`.
  - A **backup level** is `The backup level is the increment that is saved from the Full Dump. The higher the level, the further from the full dump it is.`.
  - A **level 0 backup** is `A full archive that incremental files are based on`.

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
  sudo tar -rvf /var/backups/home.tar /home
  touch ~/new_file.1 ~/new_file.2
  sudo tar --create --file=/var/backups/home.1.tar --listed-incremental=/var/log/home.snar /home
  
  ```

### Cron
#### Managing cron
Please paste the contents of `backup-cron-jobs.txt` in the space below.

  ```bash
  # Paste the contents of `backup-cron-jobs.txt` below
  2 * * * 2,4,6 sudo tar -cvf ~/data/cron/cronjob.tar ~/data/cron/Documents --wildcards "*pdf" && sudo tar -xvf ~/data/cron/cronjob.tar -C ~data/cron/exercises >/dev/null 2>&1
  ```
