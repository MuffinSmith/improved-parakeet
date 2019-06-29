# Service Discovery

## Instructions
- Launch Wireshark, and start capturing packets.

- Use Nmap to scan: `http://scanme.nmap.org`.
  - Save the results to a file called `nmap_results`.
  - **Hint**: Use `-oN` _or_ `>`. The `-oN` flag saves Nmap's normal output to a file, e.g.: `nmap http://scanme.nmap.org -oN scan_results.txt`. You could also just redirect its output with `>`, e.g.: `nmap http://scamne.nmap.org > scan_results.txt`.

- AFter the scan completes, stop Wireshark, and save the capture as `syn_scan.pcap`.

- Inspect the results of your Nmap scan. Research any unfamiliar services.
  > **Solutions**
  >   - `135/msrpc` (Microsoft RPC)
  >   - `139/netbios-ssn` (NetBIOS)
  >   - `445/microsoft-ds` (SMB)
  >   - `9929/nping-echo` (custom nping echo server)
  >   - `31337/tcpwrapped` (some custom TCP wrapped port)


- Perform a service scan with OS fingerprinting. Save this to a file called `service_scan`.
  > **Solution**: `sudo nmap -sV -O scanme.nmap.org -oN service_scan`.

- Inspect the results of your service scan. 
  - Which server does `scanme.nmap.org` use? Which version?
    > **Solution**: Apache httpd 2.4.7
  - Which operating system is running on the target?
    > **Solution**: Ubuntu running on VirtualBox.
  - Which services sit behind a firewall?
    > **Solution**: MSRPC, SMTP, microsoft-ds and NetBIOS are all behind firewalls ("`filtered`").
  