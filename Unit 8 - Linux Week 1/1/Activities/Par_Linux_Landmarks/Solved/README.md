# Linux Landmarks

In the previous exercise, you found files in a variety of different directories, such as `/home` and `/var/log`.

These are important directories on Linux systems. In this activity, you'll have an opportunity to explore these and other important locations on the file system.

## Instructions

- Move to the `/` directory, and run `ls`.
  - What does this directory contain?
    - This is the **root** directory. It contains all other files on the system.

- Move to `/etc`, and list the files it contains.
  - Use `cat` to read `/etc/passwd`.
  - `sudo cat` to read `/etc/shadow`.
  - Read `man 5 shadow`. What does the `shadow` file contain?
    - `/etc/shadow` contains the hashed passwords of every user on the system.
  - Read `/etc/hosts`. What does this file contain? Refer to the reading if you're stuck.
    - `/etc/hosts` is a local DNS database. It contains the IP <-> Hostname mappings that the server understands on its own. To resolve any IP addresses _not_ contained in this file, the server will have to query a different DNS database.

- Move to `/bin`, and list the files it contains.

- Move to `/usr/bin`, and list the files it contains.
  - Look closely at the contents of these directories, specifically at the files beginning with the letters `l`, `c`, and `t`. Do you notice anything familiar?
    - You'll notice `cd`, `ls`, and `touch`, amongst other familiar commands.

- Move to `/var`, and list the directories it contains.
  - Some of these will be unfamiliar, but what do you think the following contain?
    - `/var/backups`: Contains system backups. Surprise, surprise.
    - `/var/tmp`: Contains _temporary_ files. This is like a "scratchpad" for running processes.
    - `/var/log`: Contains log files. This is where running programs save important information about errors, warnings, etc.

- Return to `/home`. What does this directory contain?
  - `/home` contains each user's personal, private directories.

- Move to `/tmp`. What kind of data do you think this directory contains?
  - Like `/var/tmp`, `/tmp` contains temporary data.

- What's the difference between `/tmp` and `/var/tmp`?
  - Like `/var/tmp`, `/tmp` is a scratchpad for running programs. Unlike `/var/tmp`, the contents of the top-level `/tmp` directory are cleared upon reboot.

## Questions

- Read the following document before working through the questions below: <http://linuxcommand.org/lc3_lts0040.php>
  -

- What kinds of files does `/` contain?
  - `/` contains every other file on the computer.

- What kinds of files does `/etc` contain?
  - `/etc/` contains important configuration files.

- What kinds of files does `/var` contain?
  - `/var` contains "variable" files—i.e., files that change over time, such as process logs; backups; et.

- What kinds of files do `/bin`, `/usr/bin`, and `/usr/sbin` contain?
  - `/bin` and `/usr/bin` contain executables, i.e., programs that the user and/or system can run, such as `ls`.

- What's the difference between these different "bin" directories?
  - `/bin` contains programs that the system needs to survive, like `bash`.
  - `/usr/bin` contains programs that are mostly user-facing, such as `cat` and `ls`.
  - `/usr/sbin` contains programs that are used by users, but for system administration, suchas `adduser`.

- What kinds of files does `/home` contain?
   - `/home` contains each users' personal data.

- Suppose you're looking for a program called `chpasswd`. Which directories would you look in first?
  - The first places to look would be `/bin`, `/usr/bin`, and `/usr/sbin`.
  - In this case, `chpasswd` would be in `/usr/sbin`, because it's used by _users_ who are _system_ administrators.

- You've been told to find a configuration file called `fstab`. Which directory should you look in?
  - Configuration files live in `/etc`, so we'd look at `/etc/fstab`.

- An investigator tipped you that `freya` is also a malicious user. What's the first directory you'd look in to examine the files she's saved on the system?
  - The first place to look would be `/home/freya`.

- Which file would you read to get a list of all the users on the system?
  - Usernames for everyone on the system are stored in `/etc/passwd`.

- Which file would you read to get all users' hashed passwords?
  - Hashed passwords are stored in `/etc/shadow`.

- Suppose you've compromised a target machine, and you want to write a custom exploit while you're there. Which directory would you save it in to best cover your tracks?
  - A common place to save files like this is `/tmp`, because it's cleared by the system on reboot. Nefarious...
