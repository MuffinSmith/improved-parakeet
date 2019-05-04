# File Permissions
This activity will give you an opportunity to practice inspecting and setting file permissions.

## Instructions
### Setting File Permissions
- Inspect the permissions on the following files and directories:
  - `/etc/shadow`
    > **Solution**: `-rw-r-----`
  - `/etc/passwd`
    > **Solution**: `-rw-r--r--`
  - `~/.bashrc`
    > **Solution**: `-rw-r--r--`
  - The directories in `/home`
    > **Solution**: All are: `drwxr-xr-x`

- Next, create two new directories in your `~/Documents`, called `GroupFAQs` and `PrivateData`.
  > **Solution**
  >  ```
  >  cd ~/Documents
  >  mkdir GroupFAQs PrivateData
  >  ```

- In `PrivateData`, create three new files. Use any names you'd like. Remove "group" and "other" permissions from these files.
  > **Solution**
  >  ```
  >  cd ~/Documents/PrivateData
  >  touch file.one file.two file.three
  >  chmod g=,o= *
  >  ```

- In `GroupFAQs`, create three new files. Use any names you'd like. Grant "group" read access (but not write or execute), and remove "other" access to these files. Verify your changes.
  > **Solution**
  >  ```
  >  cd ~/Documents/GroupFAQs
  >  touch file.one file.two file.three
  >  chmod g=r,o= *
  >  ls -l
  >  ```

- Change back to `~/Documents`. Update the permissions for files in `GroupFAQs` such that they have "group" read _and_ write access. Verify your changes.
  > **Solution**
  >  ```
  >  cd ~/Documents
  >  touch file.one file.two file.three
  >  chmod -R g=rw,o= GroupFAQs
  >  ls -l GroupFAQs
  >  ```
