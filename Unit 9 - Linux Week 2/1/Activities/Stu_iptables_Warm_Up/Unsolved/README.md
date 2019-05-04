# iptables Warm-Up
In this exercise, you'll interpret a handful of iptables rules to prepare for later exercises on Snort attack signatures.

## Instructions

### Using iptables
Use the iptables manpages to answer the questions below: <http://ipset.netfilter.org/iptables.man.html>
- What command do you use to delete all iptables rules?
- Which command would you use to set the INPUT and OUTPUT default chains to DROP?

### Reading Rules
Read the rules below, and answer the following questions.
- What does each rule do?
Which service do these rules enable?
What would happen if the first rule were implemented without the second? Vice-versa?

  ```bash
  iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
  iptables -A OUTPUT -o eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
  ```

---
Read the rules below, and answer the following questions.
- Which devices are allowed to make connections to host port 3306?
- Which service do these rules enable?
- Why does this rule only allow traffic from this specific subnet?


  ```bash
  iptables -A INPUT -i eth0 -p tcp -s 192.168.100.0/24 --dport 3306 -m state --state NEW,ESTABLISHED -j ACCEPT
  iptables -A OUTPUT -o eth0 -p tcp --sport 3306 -m state --state ESTABLISHED -j ACCEPT
  ```

## Extension
**Note**: For further study, return to these on your own time. 

As a **challenge**, research the following about the rule below.
- What is the `nat` table?
- What is the PREROUTING chain?
- What is DNAT?
- What is the relationship between `--dport 422` and `192.168.102.37:22`?

  ```bash
  iptables -t nat -A PREROUTING -p tcp -d 192.168.102.37 --dport 422 -j DNAT --to 192.168.102.37:22
  ```