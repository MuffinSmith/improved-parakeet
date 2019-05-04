# Sudo Wrestling

- Add your new user to the sudo group to allow them to run `nano` and/or `vi` as root.
  > **Solution**: `sudo adduser <username> sudo`
  - This allows them to read and modify `root`-owned files, such as `/etc/passwd` and `/etc/shadow`

- Determine which user's account has been compromised
- Inspect `sudoers` log for evidence of brute-force attempts to `sudo cp /etc/shadow` to a directory in `/home`
  > **Solution**: `sudo grep -a 'shadow' /var/log/auth.log`
    - Should find "zeus : user NOT in sudoers"

- Identify which user was attempting `sudo`
  > **Solution**: `zeus`

- Search for other suspicious activity in that user's `.bash_history`
  > **Solution**: `sudo cat /home/zeus/.bash_history`
    - Should show: `sudo cp /etc/passwd`

- Remove that user from privileged groups
  > **Solution**: The user is only a member of one group.

- Change that user's password, _or_ remove their account
  > **Solution**: `passwd zeus` _or_ `userdel zeus`
