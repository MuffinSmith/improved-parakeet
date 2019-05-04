# iptables Warm-Up
In this exercise, you'll interpret a handful of iptables rules to prepare for later exercises on Snort attack signatures.

## Instructions

### Using iptables
Use the iptables manpages to answer the questions below: <http://ipset.netfilter.org/iptables.man.html>
- What command do you use to delete all iptables rules?
- Which command would you use to set the INPUT and OUTPUT default chains to DROP?
  > **Solutions**
  >  - `iptables --flush`, or `iptables -F`
  >  - `iptables --policy INPUT DROP`, or `iptables -PT INPUT DROP`; and `iptables -P OUTPUT DROP`

### Reading Rules
Read the rules below, and answer the following questions.
- What does each rule do?
- Which service do these rules enable?
- What would happen if the first rule were implemented without the second? Vice-versa?


  ```bash
  iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
  iptables -A OUTPUT -o eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
  ```

  > **Solutions**
  >  - The first rule allows incoming traffic to port 80. The second rule allows outgoing traffic _from_ port 80.
  >  - These services enable HTTP traffic.
  >  - If the first rule were implemented without the second, the server could listen to HTTP traffic, but not respond. If the latter were implemented without the former, the server could theoretically send HTTP responses, but wouldn't be able to "hear" HTTP requests.

---
Read the rules below, and answer the following questions.
- Which devices are allowed to make connections to host port 3306?
- Which service do these rules enable?
- Why does this rule only allow traffic from this specific subnet?


  ```bash
  iptables -A INPUT -i eth0 -p tcp -s 192.168.100.0/24 --dport 3306 -m state --state NEW,ESTABLISHED -j ACCEPT
  iptables -A OUTPUT -o eth0 -p tcp --sport 3306 -m state --state ESTABLISHED -j ACCEPT
  ```

  > **Solutions**
  >  - Only devices on the subnet `192.168.100.0/24` can connect to this machine's port 3306.
  >  - MySQL runs on port 3306 by default.
  >  - Since databases are so sensitive, access to them should be allowed by as few devices as possible. In this case, the DB is probably either a database on a private subnet which does not need to be exposed to the public Internet; or, it backs a public-facing HTTP server on the local subnet.

---
As a **challenge**, research the following about the rule below.
- What is the `nat` table?
- What is the PREROUTING chain?
- What is DNAT?
- What is the relationship between `--dport 422` and `192.168.102.37:22`?

  ```bash
  iptables -t nat -A PREROUTING -p tcp -d 192.168.102.37 --dport 422 -j DNAT --to 192.168.102.37:22
  ```

  > **Solutions**
  >  - The `nat` table sets up Network Address Translation (NAT) rules, which is important for devices being used as routers.
  >  - The PREROUTING chain contains rules that translate the source IP address of outgoing packets to match that of the routing device, _not_ the subnet IP address of the originating machine. This is called "source NAT", or SNAT, and is used to allow a device behind a router to 
  >  - DNAT stands for "destination NAT". This is the process of changing the destination IP address of a packet, but _not_ the source. This is intended to allow hosts _outside_ the router's subnet to communicate with devices on that subnet.
  >  - This rule forwards connections to `192.168.102:37:422` to `192.168.102:37:22`. This means SSH clients can connect to `192.168.102:37`'s SSH server through either port 422 or 22.
