# Creating Rules
In this exercise, you'll write Snort rules and test them against live traffic.

## Instructions
**Note**: After writing each rule, start Snort, then inspect the Snort `alert` file to check that it was fired.
---
- Attach to your Snort container. Then, open `local.rules` in nano.
  > **Solution**
  >   - `nano /etc/snort/rules/local.rules`

- Delete or comment out all of the existing rules. Then, add the rules described below.
  - Write a rule that detects telnet traffic from the public Internet to the local subnet.
  - Write a rule that detects HTTP traffic to the local subnet. It should look for content containing any of the strings/usernames `guest`, `admin`, or `administrator`.
    - **Hint**: Be sure to specify the correct destination port(s).
  > **Solutions**
  > ```bash
  > alert tcp $EXTERNAL_NET any -> any 23 (msg:"Telnet packet detected!";sid:2000000;)
  > alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS 80 (msg:"HTTP packet detected! Possible BRUTE FORCE...";content:"guest|admin|administrator";sid:2000000;)
  > ```
