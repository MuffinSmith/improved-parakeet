# Interpreting Snort Rules
In this exercise, you'll:
- Interpret the rules that fired in the previous exercise
- Interpret new rules
- Use the Snort documentation to research additional rule options

Refer to the Snort rule options documentation as you follow the instructions below: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html>

**Good luck!**

## Instructions
Explain the below ICMP Echo Reply rules. Be sure to identify the:
> **Solutions**
>   - **Action**: `alert`
>   - **Protocol**: `icmp`
>   - **Source/Destination Addresses**: `$EXTERNAL_NET any -> $HOME_NET any`
>   - **Meaning of each new rule option**
>     - `icode`: Checks for a specific ICMP code value.

```bash
alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"PROTOCOL-ICMP Echo Reply"; icode:0; itype:0; metadata:ruleset community; classtype:misc-activity; sid:408; rev:8;)

alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"PROTOCOL-ICMP Echo Reply undefined code"; icode:>0; itype:0; metadata:ruleset community; classtype:misc-activity; sid:409; rev:10;)
```
---
Explain the ICMP Unusual PING rule below. Be sure to identify the:
> **Solutions**
>   - **Action**: `alert`
>   - **Protocol**: `icmp`
>   - **Source/Destination Addresses**: `$HOME_NET any -> $EXTERNAL_NET any`
>   - **Meaning of each new rule option**
>     - `fragbits: M`: Checks if the "More Fragments" fragmentation and reserved headers are set in the IP packet. This flag indicates that this packet is just one in a stream of packets.
>     - reference:url,<url>`: Include a link to relevant documentation.


```bash
alert icmp $HOME_NET any -> $EXTERNAL_NET any (
    msg:"PROTOCOL-ICMP Unusual PING detected"; 
    icode:0; 
    itype:8; 
    fragbits:!M; 
    content:!"ABCDEFGHIJKLMNOPQRSTUVWABCDEFGHI"; depth:32;
    content:!"0123456789abcdefghijklmnopqrstuv"; depth:32;
    content:!"EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"; depth:36;
    content:!"WANG2";
    content:!"cacti-monitoring-system"; depth:65;
    content:!"SolarWinds"; depth:72;
    metadata:ruleset community; 
    reference:url,krebsonsecurity.com/2014/01/a-closer-look-at-the-target-malware-part-ii/;
    reference:url,krebsonsecurity.com/2014/01/a-first-look-at-the-target-intrusion-malware/;
    classtype:successful-recon-limited;
    sid:29456;
    rev:2;)
```

- There are multiple `content` options in this rule. 
  - **Important Note**: There's an exclamation mark in front of each content string. Use the documentation to find out what this means.
  > **Solution**: The `!` means to match packets that do _not_ have these contents.
  - Why do you suppose this rule includes so many?
  > **Solution**: This rule monitors for unusual ping activity. Each content block includes a different _trusted_ string. This rule is a "blanket check" for packets that do _not_ contain these trusted strings.
---
Explain the rule below. Be sure to identify:
> **Solutions**
>   - **Action**: `alert`
>   - **Protocol**: `tcp`
>   - **Source/Destination Addresses**: `$EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS`. This watches traffic from the public Internet to local HTTP servers.
>   - **Meaning of each new rule option**
>     - `flow:to_server,established`: Watches traffic flowing from the public Internet _into_ the server on an _established_ connection. I.e., this packet is _not_ a request to initiate a connection—it's being transferred over an existing one.
>     - `fast_pattern`: Enables fast pattern matching.
>     - `nocase`: Make the search for the content string case-insensitive.
>     - `distance:0`: Ignore `0` bytes before looking for the content string.
>     - `http_uri`: Restricts the content search to the HTTP URI field, _not_ the rest of the packet.
>     - pcre`: Allows the rule writer to specify a regular expression, so they can look for multiple patterns in a single rule.

  ```bash
  alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (
      msg:"SQL PK-CMS SQL injection attempt"; 
      flow:to_server,established; 
      content:"/default.asp?"; fast_pattern; 
      nocase; http_uri;
      content:"pagina="; distance:0; http_uri; pcre:"/pagina=[^&]*\x27/Ui";
      metadata:service http; 
      reference:url,github.com/BuddhaLabs/PacketStorm-Exploits/blob/master/1309-exploits/pkcms-sql.txt;
      classtype:web-application-attack;
      sid:32768;
      rev:1;)
  ```


- Based on the reference URL, which exploit does this rule monitor for?
  > **Solution**: This exploit watches for the `pkcms-sql` exploit.

- Based on your knowledge of SQL injection and the rule above, which of the following carries the SQLi payload? What is the name of the parameter or header that is being attacked?
  > **Solution**: This exploit is delivered via the GET query string, through the parameter `pagina`.

