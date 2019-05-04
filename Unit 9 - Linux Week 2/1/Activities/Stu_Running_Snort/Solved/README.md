# Running Snort
In this exercise, you will:
- Launch Snort on your Linux machine
- Inspect the alerts and logs it generates
- Identify which rule(s) were triggered

## Instructions
### Starting Snort
- Begin by launching Snort in packet-capture mode. Be sure to enable verbose mode, and pass the correct path to `snort.conf`.
  > **Solution**: `snort -bv -c /etc/snort/etc/snort.conf`

- Open a second terminal window and run `ping 8.8.8.8`

- Watch the packet capture to verify that you're logging traffic. Then, stop Snort with `Ctrl + C`.
  > **Solution**: `snort -bv -c /etc/snort/etc/snort.conf`

- Run: `snort --help | less`. Find out what the `-q` flag does.
  > **Solution**: The `-q` flag starts Snort in quiet mode. This prevents it from logging packets to the screen.

- Restart Snort, but pass the `-q` flag, and _not_ the `-v` flag. Note what happens. Then, stop Snort.
  > **Solution**: Run `sudo snort -bq -c /etc/snort/etc/snort.conf`. This starts Snort, but logs nothing to the console.

- Find out how to enable "full Alerts".
  > **Solution**: Use the f lag `-A full`.

- Launch Snort in quiet mode with full alerts, and put it in the background with `&`. Run `ps` to ensure that Snort is running.
  > **Solution**: `sudo snort -A full -bq -c /etc/snort/etc/snort.conf & && ps`

- Move to `/var/log/snort`. Check how many lines are in `alert` twice in a row, and note what you see.
  > **Solution**: `wc -l alert` twice in a row. You'll see that alert gets longer between runs, indicating that Snort is actively appending alerts to this file.

- Run: `head alert`. Which two alerts were logged when you first ran Snort?
  > **Solution**
  >   ```bash
  >   [**] [1:366:11] PROTOCOL-ICMP PING Unix [**]
  >   [Classification: Misc activity] [Priority: 3]
  >   01/10-21:14:56.761420 172.20.0.3 -> 172.20.0.2
  >   ICMP TTL:64 TOS:0x0 ID:9183 IpLen:20 DgmLen:84 DF
  >   Type:8  Code:0  ID:8   Seq:108  ECHO
  >
  >   [**] [1:29456:2] PROTOCOL-ICMP Unusual PING detected [**]
  >   [Classification: Information Leak] [Priority: 2]
  >   01/10-21:14:56.761420 172.20.0.3 -> 172.20.0.2
  >   ICMP TTL:64 TOS:0x0 ID:9183 IpLen:20 DgmLen:84 DF
  >   ```
  > The two alerts that got logged were PROTOCOL-ICMP PING Unix and PROTOCOL-ICMP Unusual PING detected.

- Run: `tail alert`. Which alert(s) was/were logged most recently?
  > **Solution**
  >   ```bash
  >   [**] [1:408:8] PROTOCOL-ICMP Echo Reply [**]
  >   [Classification: Misc activity] [Priority: 3]
  >   01/10-22:15:14.046234 172.20.0.2 -> 172.20.0.3
  >   ICMP TTL:64 TOS:0x0 ID:30474 IpLen:20 DgmLen:84
  >   Type:0  Code:0  ID:8  Seq:3040  ECHO REPLY
  >   ```
  > In this case, we see a PROTOCOL-ICMP Echo Reply alert.

- Which IP addresses did Snort log traffic to/from?
  > **Solution**: The directory listing indicates that Snort received traffic to/from IP addresses 172.18.0.1; 172.18.0.2; and 172.18.0.3.

### Finding Rules
- Move to `/etc/snort/rules`.
  > **Solution**: `cd /etc/snort/rules`

- Find out which rules fired the alerts in `/var/log/snort/alert`.
  > **Solution**: Run the below to find the right rules.
  >   - `grep -ni "protocol-icmp echo reply" community.rules` identifies rules 408 and 409.
  >  - `grep -ni "protocol-icmp unusual ping detected" community.rules` identifies rule 29456.
  >  - `grep -ni "protocol-icmp ping unix" community.rules` identifies rule 366.

- One of the rules includes two URLs to articles on Krebs on Security. Use them to determine which major corporation was affected by an attack this rule would flag.
  - **Solution**: The links show that Target was hit by a
