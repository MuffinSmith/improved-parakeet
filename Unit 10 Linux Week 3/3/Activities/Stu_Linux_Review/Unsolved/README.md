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

- Create a file called `/tmp/server.logs`. Write a command that sets its permissions to `rwx-rw-r--`.
  - **Note**: Use both octal _and_ symbolic notation.

- Create a new user, called `guest`, whose default shell is `/bin/bash`.
  - **Note**: Use `adduser` .

- Set your `guest`'s password to `tsueg`.

- Add your user to the `sudo` group.

### Advanced Bash
These exercises will give you practice with:
- Flow control operators
- Redirection
- For loops
- Expansion

You'll build an increasingly complex `ping` command that combines most of these tools. Then, you'll use expansion and for loops to enumerate valid usernames.

---

#### Ping
- Use nano to create and open a file called `ping_challenge.sh`.

- Store the value `8.8.8.8` in a variable called `IP`.

- Use your variable to ping `8.8.8.8` once.
  - **Note**: Use the `-c` flag.

- Use a flow control operator to `echo` the message `'8.8.8.8' is UP` if the ping succeeds, and `'8.8.8.8' is DOWN` if it fails.
  - **Note**: Use the `IP` variable in your `echo` commands.

- Redirect stderr and stdout from your `ping` command to `/dev/null`.

- Test your script by running: `bash user_enum.sh`.

#### Getting User Information
In this exercise, you'll write a for loop that prints out whether a given username exists on the machine. It will
- Read a list of usernames from a text file
- Run `id` against each username
- Echo `<username> exists!` if the command succeeds. It will print nothing if it fails.

**Note**: Consider this a **challenge**! Feel free to come back to it after the other exercises if necessary.

---

- Use nano to create and open a file called `ping_challenge.sh`.

- Use a command expansion to write a loop that prints every username in the file `usernames.txt`.
  - **Note*: Use `cat`.**

- Update your loop to run `id <username>` for each username.

- Use flow control operators to print the message: `<username> exists!` if `id` succeeds. Do _not_ print a message if it fails.

- Test your script by running: `bash user_enum.sh`.

### Archives
In this series of exercises, you'll practice:
- Archiving directories
- Excluding files from a tarball
- Extracting a tarball to a specific directory

**Note**: Your solutions to the below will be single commands. Do _not_ store them in a script file.

---

- Use `tar` to create a bzip2 archive of your `Projects` directory.

- Use `tar` to create a gzip archive of your home directory (`~`), but _exclude_ the `Documents` folder.

- Use tar to unpack the tarball from the previous step into `/tmp`.

### Cron
In this exercise, you'll practice writing cron jobs for important tasks.

**Note**: Please simply write your solutions in a text file, called `cron_challenge.txt`. You do not need to add them to your crontab.

---

- Write a cronjob that creates a bzip2 archive of the `/home` directory every Sunday.

- Write a cronjob that creates a gzip archive of the `/var/log` directory every day at 5AM.
