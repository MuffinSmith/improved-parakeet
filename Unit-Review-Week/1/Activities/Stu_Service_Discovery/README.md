# Service Discovery

## Instructions
- Launch Wireshark, and start capturing packets.

- Use Nmap to scan: `http://scanme.nmap.org`.
  - Save the results to a file called `nmap_results`.
  - **Hint**: Use `-oN` _or_ `>`.

- AFter the scan completes, stop Wireshark, and save the capture as `syn_scan.pcap`.

- Inspect the results of your Nmap scan. Research any unfamiliar services.

- Perform a service scan with OS fingerprinting. Save this to a file called `service_scan`.
  - **Hint**: Check the `--help`.

- Inspect the results of your service scan. 
  - Which server does `scanme.nmap.org` use? Which version?
  - Which operating system is running on the target?
  - Which services sit behind a firewall?
