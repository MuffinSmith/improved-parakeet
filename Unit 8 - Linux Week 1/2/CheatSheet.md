# Day 2 Cheat Sheet - Linux

## Key Terms

- **File or Directory Owner**: The 'owner' is the main user assigned to a file or directory.
  > **Example**: The owner of a file/directory is usually the user that created said file/directory. When looking at an file/directory's permissions, the owner's permissions are represented by the first set of `rwx` listed. When you create a file or directory, you become the `owner` of that file or directory. If a program creates an file/directory, the owner of the file/directory is not the program, but rather the user that started the program.

- **File or Directory Group**: The 'group' of users or programs assigned to a file or directory.
  > **Example**: The group of a file or directory represents all users that are a member of that group. In other words, it represents an entire group of users. When viewing an file/directory's permissions, the group's permissions are represented by the second set `rwx` letters.


- **File or Directory Other/World**: A category that represents all 'other' users on a system.
  > **Example**: The Other/World category of a file/directory represents any user that is not in the group assigned to the file/directory, and it is not the owner of that file/directory. In other words, it is any other user that is not directly associated with that file/directory. When viewing an file/directory's permissions, the 'Other/World' permissions are represented by the third set `rwx` letters.

- **File Permissions**: The set of 10 permissions flags assigned to every file/directory.
  > **Example**: -rwxrwxrwx - The first flag represents the file type. If it is a directory, a 'd' is shown. If it is a file, a `-` is shown. The remaining 9 flags are comprised of 3 groups of `rwx`. `r` for `read`, `w` for `write` and `x` for `execute`. Each of the 3 sets of letters represent an entity and it's respective `read`, `write`, and `execute` permissions for that file/directory. The first set of `rwx` represent the `owner's permissions`. The second set of `rwx` represent the `group's permissions` and the third set of `rwx` represents the permissions of all other users on the system. The letters in each set of `rwx` never change position. If a certain permission is missing it is represented by a `-`. e.g. `drwxr-xr--` shows a directory where the owner has full permissions to read, write and execute, the group can read and execute but not write, and all other users can only read.

- **Symbolic Notation**: When changing an file/directory's permissions the letters `r`, `w`, and `x` are used directly within a command.
  > **Example**: `+x` would add execute privileges and `-w` would remove write privileges.

- **Octal Notation**: When changing a file/directory's permissions numbers are used to represent the respective `r`, `w`, and `x`.
  > **Example**: Each letter in a group of `rwx` is assigned a number if you want to set it. `r` always equals 4, `w` always equals 2, and `x` always equals 1. If you don't want to set that permission, it's value is 0. The octal notation is the sum of the values assigned to each letter. If you want to set permissions to only read, the number is 4. If you want to read and write, add the numbers for `r` and `w` together and the number is 6. If you want read and execute, the number is 5. `rwx` would be equal to 7. This way, you can represent the permissions of the user, group and other with just 3 numbers. e.g. 755 would translate to rwxr-xr-x.

## Key Commands

### General thing to discuss

#### sudo

Stands for 'Super User Do'. It's the command you have to use if you want to invoke the system permissions of the root user (also known as the super user).

```bash
# Show the contents of the /etc/shadow file
sudo cat /etc/shadow
```
```bash
# Update the list of programs offered in the `apt` repository
sudo apt update
```
Many files/directories are only accessible by the root user. Also many programs require root permissions to run. If you are not logged in as root, you either have to switch your login to the root user, or you can use `sudo` command to run a single command with root permissions. Note: In order to use the 'sudo' command, your user has to be part of the 'sudo' group.

#### su

Stands for 'Switch User'. If you do not specify a user to switch to, the default is root.

```bash
# Switch your login to the root user and 'preserve' your current environment.
su -p
```
#### visudo

You _must_ use `visudo` to edit the `/etc/sudoers` file.

```bash
# Edit the /etc/sudoers file and validate that it is not damaged before saving.
sudo visudo -c
```

#### id

The id command gives you the UID, GID, and group information for a user.

```bash
#Show the UID, GID, and group information for user randal.
id randal
```
If no user is specified, the current user's info is displayed.

#### ls -l

List the 'long' form of files and directories in your present working directory.

```bash
#List 'all' the files in 'long' form with 'human' readable file sizes.
ls -alh
```
This is used to see the permissions of files/directories, the username and group of the file/directory owner, the file/directory size in bytes and the time of it's last modification.

#### adduser

`adduser` makes it easy to:
- Customize the user creation process
- Set user passwords
- Create and manage groups and group membership

```bash
# Add a new user with the username 'ralph'
adduser ralph
```

#### groupadd

groupadd allows you to make and create groups on the system.

```bash
# Create a new group named 'developers'
groupadd developers
```
#### usermod

usermod allows you to change many parameters of a user. It is typically used to change a user's primary group, or add secondary groups.

```bash
# Add the user bertha to the group hr_administrators
usermod -aG hr_administrates bertha
```

#### chmod

You change permissions with the command `chmod`, which stands for "change mode".

```bash
# Change the permissions to rwx for the user, rw- for the group and --- for everyone else.
chmod u+rwx,g=rw,o= permissions_file
```

You can also use chmod with octal notation to set permissons.
```bash
# Change the permissions to rwx for the user, rw- for the group and --- for everyone else.
chmod 760 permissions_file
```
#### chown

Stands for 'change owner'. When you change the owner, you also have to specify the group that you are assigning.

```bash
# Change the owner to bernard and the group to finance for the file spreadsheet
chown bernard:finance spreadsheet
```
Anything else about the Command
