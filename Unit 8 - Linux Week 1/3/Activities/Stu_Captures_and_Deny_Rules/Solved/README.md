# Warm-Up

In this exercise, you'll review the major takeaways from the previous lessons, including:
  - Packet Captures with tcpdump
  - Implement `deny` rules with `ufw`

**Good luck!*

### Packet Captures with tcpdump

Refer to the tcpdump Primer: <https://danielmiessler.com/study/tcpdump/>

- On the Virtual Machine, move to `/tmp`.
  - **Solution**: `cd /tmp`

- Start a packet capture, and save it to the file `mystery.pcap`.
  - **Solution**: `tcpdump -i any -w mystery.pcap`

- Open the capture with Wireshark, and filter for `tcp.port == 80`. Right-click on one of the TCP packets, and click **Follow Stream**.Based on the SYN
  - Based on what you know about NMap, what does the information in the **Info** column tell you about this traffic?
    - **Solution**: The sequene of TCP flags suggest a SYN scan: First `SYN`, then `SYN ACK`, then `RST`.
  - Identify the IP Address of the attacking machine.
    - **Solution**: In my environment, the attacking machine has IP Address `172.22.0.2`.

### Access Control with UFW

- Start the firewall.
  - **Solution**: `ufw start`

- Implement a deny rule with UFW that blocks all traffic from the offender.
  - **Solution**: `ufw deny from 172.22.0.2 to any`

- List your firewall rules to ensure the rule was added, and use tcpdump to verify that it's in effect.
  - **Solution**
    - `ufw status verbose`
    - `tcpdump -n -i any` should print nothing from IP Address 172.22.0.2.
