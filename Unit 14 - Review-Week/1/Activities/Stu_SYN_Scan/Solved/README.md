# SYN Scan

## Instructions
- Launch Wireshark, and open the `syn_scan.pcap` trace you took in the previous exercise.

- Filter for packets sent from your IP address to port 81 of `45.33.32.156` (the IP address of `scanme.nmap.org`). Note the TCP flags on each packet.
  - Is port 81 open, closed, or behind a firewall? How do you know:
    > **Solution**: Port 81 is closed. You can tell because the server just sends a RST response.

  - Update your filter to `port 135`. Note the TCP flags on each packet. 
    - Is port 135 open, closed, or behind a firewall? How do you know:
    > **Solution**: Port 135 is behind a firewall (filtered). You can tell because the server never sends a response—we only see Nmap's four SYN packets. This means there's a firewall dropping them before they ever get to the server.

  - Update your filter to `port 139`. Note the TCP flags on each packet. 
    - Is port 139 open, closed, or behind a firewall? How do you know:
    > **Solution**: Port 139 is behind a firewall (filtered). You can tell because the server never sends a response—we only see Nmap's four SYN packets. This means there's a firewall dropping them before they ever get to the server.

  - Update your filter to `port 443`. Note the TCP flags on each packet. 
    - Is port 443 open, closed, or behind a firewall? How do you know:
    > **Solution**: Port 443 is closed; the server responds with a RST packet.

  - Update your filter to `port 80`. Note the TCP flags on each packet. 
    - Is port 80 open, closed, or behind a firewall? How do you know:
    > **Solution**: Port 80 is open; the server responds with a SYN/ACK packet.

- Look at the packets sent to/from port 80.
  - Was a connection established?
  - What indicates that a connection was (or was not) established?
  > **Solution**: No. You can tell because the capture only contains a SYN -> SYN/ACK exchange. If a connection had been opened, it would have been: SYN -> SYN/ACK-> ACK.

- Use the **Statistics** options to determine how many bytes of data you sent to `scanme.nmap.org`.
  > **Solution**: 172 kilobytes.
