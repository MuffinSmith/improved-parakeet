## Scavenger Hunt Review

In this exercise, you'll use everything you've learned to find a series of "flags" on your Linux machine. 

### Solutions Guide:

- Find an unusual-looking log file in one of the `norse-guder` directories.
  
  **Solution:**
   
   - Run `groups user` for each user on the system.
   - Run `find /home/ -iname '*.log' and you should see a `webserver.log` in the home directory of the user Loki.

- Use awk and/or sed to figure out the distinct count of IP Addresses in this log file.
  
   **Solution:**
  
     - Use `head` to read the log file and note which column contains IP addresses. 
     - Use this number in an awk command, e.g.: Should be `awk '{print $1}' webserver.log`
     - Next, pipe to `sort` and then `uniq`: `awk '{print $1}' webserver.log | sort | uniq`. This produces a list of only unique IP addresses.
     - Finally, pipe to `wc -l` to count lines: `awk '{print $1}' webserver.log | sort | uniq | wc -l`. You should count `51` IP addresses.

- Find the members of the `hackers` group and use the IP address count from the previous step as their password.
 
  **Solution:**
 
    - To find the members of the hackers group, you could run `for i in $(ls /home); do groups $i; done | grep hacker` or something similar. Or just run `groups <user>` for each user listed in the home directory again.
    - After trying `51` in various ways, you should be able to login to the user `asgard` using `fiftyone` for the password.

- Login using the credentials found in the last step and look for a file with permissions: `-r--------` in that user's files. Make sure this file contains information about a person.
  
   **Solution**: 
   
    - There is a `contacts` directory in `~/asgard/contacts`. 
    - Move into that directory and us `ls -l`. 
    - You should see a contact with the permissions `-r--------` named `mickey.reichert`. 
    - Run `cat mickey.reichert` to reveal `hera iloveyou`.

- Use the contents of this file to log into this user's account.
   
   **Solution:** 
   - Login to the account `hera` using the password `iloveyou`

- Hackers planted a file in the directory the kernel is stored. Find it.
   
   **Solutions**: 
   - You'll find the data file: `/boot/blackhats.list`.

- Calculate the SHA256 hash of the `/boot/blackhats.list` file
  > **Solution**: Run: `"sha256sum /boot/blackhats.list" should output:" 97d054a8b3b6152e565a4e152f1db64a90cbbc5892c8809260148591b03559eb  blackhats.list"`

- Submit the result of the above computation.
  > **Solution**:`97d054a8b3b6152e565a4e152f1db64a90cbbc5892c8809260148591b03559eb  blackhats.list`


---
© 2019 Trilogy Education Services