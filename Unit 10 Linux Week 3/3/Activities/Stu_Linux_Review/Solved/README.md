# Linux Review
This exercise is a comprehensive review of everything you have learned over the preceding two weeks.

Use your VM to develop and test your solutions. Create a directory in `~/Documents/LinuxReview`, and move into it. You'll save your work here.

You will have another opportunity to practice these tools in the Homework—consider this practice.

**Good luck!**


## Instructions
### The Basics
In this section, you'll review Linux fundamentals, including:
- File permissions
- Users and Groups
- Authentication with `sudo` and `su`

**Note**: Your solutions to the below will be single commands. Do _not_ store them in a script file.

---

- Create a file called `/tmp/server.logs`. Write a command that sets its permissions to `rw-rw-r--`.
  - **Note**: Use both octal _and_ symbolic notation.
  > **Solutions**
  > ```bash
  > $ chmod u=rw,g=rw,o=r /tmp/server.logs
  > $ chmod 664 /tmp/server.logs
  > ```

- Create a new user, called `guest`, whose default shell is `/bin/bash`.
  - **Note**: Use `adduser` .
  > **Solution**
  > ```bash
  > $ sudo adduser guest --shell /bin/bash
  > ```

- Set your `guest`'s password to `tsueg`.
  > **Solution**
  > ```bash
  > $ sudo passwd guest
  > # Enter: `tsueg`
  > ```

- Add your user to the `sudo` group.
  > **Solution**
  > ```bash
  > $ usermod -aG sudo guest
  > ```

### Advanced Bash
These exercises will give you practice with:
- Flow control operators
- Redirection
- For loops
- Expansion

You'll build an increasingly complex `ping` command that combines most of these tools. Then, you'll use expansion and for loops to enumerate valid usernames.

---

#### Ping
**Note**: The solution is contained in [ping_challenge.sh](ping_challenge.sh), and duplicated below.

> **Solution**
> ```bash
> #!/bin/bash
>
> ip="8.8.8.8"
> ping -c 1 $ip > /dev/null 2>&1 && echo "$ip is up!" || echo "$ip is down!"
> ```

#### Getting User Information
**Note**: The solution is contained in [user_enum.sh](user_enum.sh), and duplicated below.

  > **Solution**
  > ```bash
  > #!/bin/bash
  >
  > for USER in $(cat usernames.txt); do
  >   id $USER > /dev/null 2>&1 && echo "$USER exists!"
  > done
  > ```

### Archives
In this series of exercises, you'll practice:
- Archiving directories
- Excluding files from a tarball
- Extracting a tarball to a specific directory

**Note**: Your solutions to the below will be single commands. Do _not_ store them in a script file.

---

- Use `tar` to create a bzip2 archive of your `Projects` directory.
  > **Solution**: `tar cfvj projects.tar.bz2 ~/Documents/Projects`

- Use `tar` to create a gzip archive of your home directory (`~`), but _exclude_ the `Documents` folder.
  > **Solution**: `tar cfvz home.tar.gz ~ --exclude="~/Documents"`

- Use tar to unpack the tarball from the previous step into `/tmp`.
  > **Solution**: `tar xvfz home.tar.gz -C /tmp`

### Cron
**Note**: Solutions are contained in [cron_challenges.sh](cron_challenges.sh), duplicated below.

---

- Write a cronjob that creates a bzip2 archive of the `/home` directory every Sunday. Save it in `/var/backups`.
  > **Solution**: `* * * * 7 tar cfvj /var/backups/home.tar.bz2`

- Write a cronjob that creates a gzip archive of the `/var/log` directory every day at 5AM. Save it in `/var/backups`.
  > **Solution**: `* 5 * * * tar cfvz /var/backups/logs.tar.bz2`
