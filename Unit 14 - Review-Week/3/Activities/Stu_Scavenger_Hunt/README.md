## Scavenger Hunt Activity File

In this exercise, you'll use everything you've learned to find a series of "flags" on your Linux machine. 

This exercise is meant to be **challenging**, and _will_ take time. Don't be afraid to ask for help, and be sure to refer to the documentation and notes from previous classes.

#### Instructions

- Find an unusual-looking log file in one of the `norse-guder` directories.
  - **Hint**: Find out which users are in the `norse-guder` group.
  - **Hint**: Use `find` to look for logs.

- Use awk and/or sed to figure out the distinct count of IP Addresses in this log file.
  - **Hint**: Use `awk` or `sed` to filter for IP addresses. Then, pipe to a new command line tool that removes duplicates. Finally, pipe to a command that counts lines.

- Find the members of the `hackers` group and use the IP address count from the previous step as their password.
 - **Hint**: If you found "24", maybe try `24`, `twenty-four`, etc.

- Find the file with permissions: `r-------x`. Make sure this file contains information about a person.
  - **Hint**: Use `ls` with special flags.

- Use the contents of this file to log into this user's account.

- Hackers planted a file in the directory that the kernel is stored. Find it.

- Calculate the SHA256 hash of the file you found in `/boot`.

- Submit the result of the above computation.
