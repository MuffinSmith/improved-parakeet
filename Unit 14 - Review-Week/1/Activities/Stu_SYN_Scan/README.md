# SYN Scan

## Instructions
- Launch Wireshark, and open the `syn_scan.pcap` trace you took in the previous exercise.

- Filter for packets sent from your IP address to port 81 of `45.33.32.156` (the IP address of `scanme.nmap.org`). Note the TCP flags on each packet.
  - Is port 81 open, closed, or behind a firewall? How do you know:

  - Update your filter to `port 135`. Note the TCP flags on each packet. 
    - Is port 443 open, closed, or behind a firewall? How do you know:

  - Update your filter to `port 139`. Note the TCP flags on each packet. 
    - Is port 443 open, closed, or behind a firewall? How do you know:

  - Update your filter to `port 443`. Note the TCP flags on each packet. 
    - Is port 443 open, closed, or behind a firewall? How do you know:

  - Update your filter to `port 80`. Note the TCP flags on each packet. 
    - Is port 80 open, closed, or behind a firewall? How do you know:

- Look at the packets sent to/from port 80.
  - Was a connection established?
  - What indicates that a connection was (or was not) established?

- Use the **Statistics** options to determine how many bytes of data you sent to `scanme.nmap.org`.

### Connect Scans
- Next, launch Wireshark, and start a capture. 

- Run a TCP connect scan against `nmap.scanme.org`. After the scan runs, stop your Wireshark capture.

- Inspect the statistics for this scan. How many bytes did you send?
