# Users and Groups

## Instructions

### Research

- Use `whoami` to print your username.
  > **Solution**: `whoami` prints `student`.

- Use `id` to print your UID, group id, and other permissions info.
  > **Solution**: `id`

- Use `id <username>` to print out information about the other five (personal!) users on the system.
  - In case you forgot, where can you find out what these usernames are?
    > **Solution**: The usernames are available by running `ls /home`, or `cat /etc/passwd`.
  - Record the output from this series of commands to answer the questions below.
    > **Solution**
    >  ```bash
    >  id freya
    >  id loki
    >  id tyr
    >  id balder
    >  id odin
    > ```

- Use `groups <username>` to print the groups you and the other users belong to.
  - Record the output from this series of commands to answer the questions below.
    > **Solution**
    >  ```bash
    >  groups freya
    >  groups loki
    >  groups tyr
    >  groups balder
    >  groups odin
    > ```
### Adding Users and Groups

- Add a new user 
  > **Solution**: `useradd <username>`

- Change your new user's password.
  > **Solution**: `passwd <username>`

- Add a user using the command demonstrated by the instructor.
  > **Solution**: `useradd <username>`

- Change your new user's primary secondary group to `norse-guder`.
  > **Solution**: `usermod -aG norse-guder`

- Check that this group assignment worked.
  > **Solution**: `id <username>` should list `norse-guder` as a secondary group.


## Questions

- What's the advantage of allowing multiple users to have accounts on a single machine?
  > **Solution**: It allows multiple users to share files and programs on a single system. 

- What is the main purpose of groups?
  > **Solution**: The main purpose of groups is to allow related users to share access to common files.

- Which command do you use to add a user? There are two possible answers.
  > **Solution**: adduser`, which prompts for a password
  > **Solution**: useradd`, which creates a user withou ta password

- Which command do you use to change a user's password?
  > **Solution**: passwd <username>`

- Which command do you use to:
  - Change a user's primary group?
    > **Solution**: `usermod +g <primary group name>`
  - Change a user's secondary group?
    > **Solution**: `usermod -aG <secondary group name>`

- Your user, `loki`, is in the primary group `norse-guder`. Your new user is in `norse-guder` as a secondary group.
  - If your new user creates a file, can `loki` read it?
    > **Solution**: Yes; `loki` would have read access to new files created by the new user.
  - If `loki` creates a file, can your new user read it?
    > **Solution**: Yes; the new user has read access to any file `loki` creates, because they are a secondary member of `norse-guder`.
  - If `loki` creates a file, what is that file's default group owner?
    > **Solution**: The file's default group owner is `norse-guder`.
  - If your new user creates a file, what is that file's default group owner?
    > **Solution**: The default owner of files created by the new user is `<new user's username>`.
