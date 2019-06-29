# General Review

#### Solutions: 
   
- What are some Text Editors?   
   - **Solution**: 
   `nano`,
   `vim`,
   and `emacs`

- What is the Top of the Linux file structure?
  - **Solution**: `/root`

- Name the directory that contains:
  - Binaries: **`/bin`, `/usr/bin`, `/usr/sbin`**
  - Files associated to the Kernel: **`/boot`**
  - Log Files: **`/var/log`**
  - Temporary Files: **`/tmp`, `/var/tmp`**
  - Configuration Files: **`/etc/`**
  - Process Files: **`/proc`**
  - Files the user wants to save: **`/home`**

- Name the command you use to:
  - Install a package: **`apt install <package>`**
  - Add a user: **`adduser`, `useradd`**
  - Change a password: **`passwd <user>`**
  - Create a new group: **`groupadd <group>`**
  - Add a user to a group: **`usermod -aG <group> <username>`**
  - Check which groups you're in: **`groups`**
  - Find your user ID: **`id`**

- What are the 3 types of file permissions?
  
  - **Solution**: Owner, Group, and World/Other permissions.

- Which command displays a file's permissions?
  
  - **Solution**: `ls -l <filename>`

- Which file gets modified when a user is added to the system?
  
  - **Solution**: `/etc/passwd`

- Which file contains hashed passwords?
  
  - **Solution**: `/etc/shadow`

- How can you tell which algorithm was used to hash a password in the file above? 
  
  - **Solution**: Look at the number in the dollar signs. E.g., `$6$` indicates a sha512-crypt hash.

- Which command changes file permissions?
  
  - **Solution**: `chmod`

- What are the 2 types of ways to change file permissions?
  
  - **Solution**: Symbolic and octal.

- What is the command to change ownership permissions?
   
  - **Solution**: `chown`

- How do you edit the sudoers file?
  
  - **Solution**: `visudo`

- How do you use sudo?
  
  - **Solution**: `sudo <command>`

- What is the command to switch to another user?
  
  - **Solution**: `su`

- What is the command to archive files?
  
  - **Solution**: `tar cvf <archive name> <files>`

- What is the command to view running processes?
  
  - **Solution**: `top` lists them dynamically. `ps` lists them statically.

- Which two commands can be used to kill processes? Which one requires a PID?
  
  - **Solution**: `kill <PID>` and `killall <Process Name>`. Only `kill` requires a PID.
