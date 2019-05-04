# Interpreting iptables Rules

In this exercise, you'll combine research with what you know about `iptables` to interpret common firewall rulesets, extracted from real configurations.

You'll be presented a series of `iptables` rules, each of which comes with a set of questions. Some answers you'll already know from lecture. Others, you'll have to research.

Any questions you need to research can be found in the `iptables` user manual, which you can access on the command line with: `man iptables`.

Recall that you can search the manpages for a specific flag with:
  - `man iptables`
  - `/-[flag]`

So, if you want to find out what the `-F` flag does, you'd open the `iptables` manual, then type: `/-F`, and hit enter. Press 'n' to scroll through search results, and you'll hae your answers in no time.

**Good luck!**

## Instructions

### Flushing the T...able?

- Sysadmins often write scripts that set up their `iptables` rules automatically. One of the first things many administrators do before configuration is clear all existing rules, so they can start fresh.

- The snippet below contains a series of commands from a configuration script that clear `iptables` rules. Read them, and use the manpages to answer the questions below.

  ```
  # Clear existing rules
  iptables -F
  iptables -F -t nat
  iptables -X
  iptables -P INPUT DROP
  iptables -P OUTPUT DROP
  iptables -P FORWARD DROP
  ```
#### Questions

- What do the manpages say about the `-F` flag?
  - **Solution**: `-F` _flushes_ a chain.

- What do the manpages say about the `-t` flag? What does `nat` represent in the second line of the above snippet?
  - **Solution**: `-t` specifies a table. With `-F`, it specifies a table to _flush_. In this case, we drop all of the firewalls `nat` rules.
  
- What do the manpages say about about the `-X` flag? 
  - **Solution**: `-X` deletes a specified chain.

- What do the manpages say about about the `-P` flag? 
  - **Solution**: `-P <chain> <target>` sets the policy for `<chain>` to `<target>`.

- Using the above, explain, in English, what the following lines from the configuration do.
  - **Solution**: `iptables -F`: Flushes all `iptables` rules.
  - `**Solution**: iptables -P INPUT DROP`: By default, _drop_ all _incoming_ connections.
  - `**Solution**: iptables -P OUTPUT DROP`: By default, _drop_ all _outgoing_ connections.
  - `**Solution**: iptables -P FORWARD DROP`: By default, _drop_ all packets that use this server as a router.

#### INPUT Rules

- Review and research the snippet, then answer the questions below.

  ```
  # The subnet this server lives on
  SUBNET = 192.168.10.0/24

  # State rules
  iptables -A INPUT -m state --state INVALID -j LOG --log-prefix "DROP INVALID "
  --log-ip-options --log-tcp-options
  iptables -A INPUT -m state --state INVALID -j DROP
  iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
  
  # ACCEPT rules
  iptables -A INPUT -i eth1 -p tcp -s $SUBNET --dport 22 --syn -m state  --state NEW -j ACCEPT
  iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
  ``` 

#### Questions

- In the first rule, the `--log-ip-options` and `--log-tcp-options` flags simply tell `iptables` log traffic it intercepts.
  - **Solution**: It's crucial because it allows us to understand attacks that occurred in the past (forensics); identify attacks in progress (intrusion detection); and understand what malicious activity looks like in general (research).

- What do the manpages say about the `-A` flag?
  - **Solution**: `-A` _appends_ a rule to the current list of rules.

- What do the manpages say about the `-m` flag?
  - **Solution**: `-m` specifies a _match_ to use in this rule. A match is an extension module that tests for a specific, special property.

- After  the `--state` flag in the first three rules, we see a few different values: INVALID, ESTABLISHED, and RELATED. NEW is also a possible value, which you'll see in the next section. Refer to the section on **The Connection Tracking Module** in this document, and define each below: <https://www.booleanworld.com/depth-guide-iptables-linux-firewall/>.
  - **Solution**: INVALID: The incoming packet doesn't have a proper state.
  - **Solution**: ESTABLISHED: The incoming packet belongs to an open connection.
  - **Solution**: RELATED: The incoming packet is related to another, already ESTABLISHED connection. E.g., `FTP-DATA` channels are _related_ to `FTP` channels.
  - **Solution**: NEW: The incoming packet is _initiating_ a connection.

- According to the manpages, `-j` specifies a chain to _jump_ to if the packet matches the rule `-j` appears in.
  - Look at the second rule under the `# State Rules` in the snippet above. Suppose a packet matches this rule. Given the `-j` flag, what will the firewall do with the packet next?
    - **Solution**: It will DROP the packet.

- The rules in the `# ACCEPT` section are a little more complicated. Let's work through them together.

- Consider the first: `iptables -A INPUT -i eth1 -p tcp -s $SUBNET --dport 22 --syn -m state  --state NEW -j ACCEPT`. 

- This is a doozy, so here's the breakdown:
  - `-A INPUT` says: "Append this rule to the end of the INPUT chain."
  - `-i eth1` says: "Apply this rule to packets coming in from the `eth1` network interface."
  - `-p tcp` says: "Apply this rule to packets sent over `tcp`."
  - `-s $SUBNET` says: "Only accept TCP packets sent from the local subnet..." (continued below)
  - `--dport 22` says: "...connecting to port 22..." (continued below)
  - `--syn` says: "...if they have _only_ the `SYN` flag set."
  - `-m state --state NEW` says: "Only accept packets that meet these conditions if they meet the previous conditions _and_ are starting a new connection."
  - `-j ACCEPT` says: "If the packet matches the preceding conditions, let it through!"

- In English, this rule says:
  - "I'm adding a rule to the input chain. The rule is: _Only_ allow TCP packets to connect to port 22 on this server if they are initiating a NEW connection; have _only_ the SYN flag set; and come from within the local subnet."
  - Port 22 is for SSH, so we could also say: "I'm adding a rule to the input chain. The rule is: _Only_ allow TCP packets to connect to port 22 on this server if they are initiating a NEW connection; have _only_ the SYN flag set; and come from within the local subnet."

- Given the above explanation, what do you think the final rule specifies?
  - Research what the ICMP protocol is used for.
    - **Solution**: ICMP is used by the `ping` utility to determine if hosts on a network are reachable.
    - **Solution**: The final rule says: "Accept all ping messages sent to this server that are 'echo requests'."
