# Sudo Wrestling

- Add your new user to the sudo group to allow them to run `nano` and/or `vi` as root.
  - This allows them to read and modify `root`-owned files, such as `/etc/passwd` and `/etc/shadow`

- Determine which user's account has been compromised

- Inspect `sudoers` log for evidence of brute-force attempts to `sudo cp /etc/shadow` to a directory in `/home`

- Identify which user was attempting `sudo`

- Search for other suspicious activity in that user's `.bash_history`

- Remove that user from privileged groups

- Change that user's password, _or_ remove their account
