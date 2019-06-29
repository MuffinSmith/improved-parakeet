## Interpreting Snort Rules

### Scenario

Because of the recent SQL injection attack, one of your technicians has installed Snort onto your network. Your technician has downloaded community Snort rules and has asked you to help them interpret them. Given the following list of rules, you will need to identify what each rule does to contribute to the overall network security. 

In this exercise, you will:

- Interpret rules that fire in response to suspicious ping probes.
- Use the Snort documentation to research additional rule options.

Refer to the Snort rule options documentation as you follow the instructions below: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html>

**Good luck!**

### Instructions

#### 1. Explain the following ICMP Echo Reply rules. Be sure to identify the:
- Action
- Protocol
- Source/destination addresses
- Meaning of each new rule option

```bash
alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply"; 
    icode:0; itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:408; 
    rev:8;)

alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply undefined code"; 
    icode:>0; 
    itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:409; 
    rev:10;)
```

action - Alert
protocol - icmp
source - anything soutside the network
destination - anything inside the network
meaning - the first one generates an alert when someone outside the network tries to ping the home network and the second one reports any other icmp requests

---

#### 2. Explain the ICMP Unusual PING rule below. Be sure to identify the:
- Action
- Protocol
- Source/destination addresses
- Meaning of each new rule option

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

action - alert
protocol - icmp
source - internal network
destination - external network
meaning - generates an alert if a computer on the internal network makes a weird ping to outside the network
looking for a packet that is fragmented
the content fields are ignored and considered safe packets

**Follow-Up Questions** regarding the multiple `content` options in this rule:
  - There's an exclamation mark in front of each content string. Use the documentation to find out what this means.
  - Why do you suppose this rule includes so many?

its how the payload detection works. each one is looking for that content inside a packet
---

#### 3. Explain the rule below. Be sure to identify:
  - Action
  - Protocol
  - Source/destination addresses
  - Meaning of each new rule option

  ```bash
  alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (
      msg:"SQL PK-CMS SQL injection attempt"; 
      flow:to_server,established; 
      content:"/default.asp?"; fast_pattern; nocase; http_uri;
      content:"pagina="; distance:0; http_uri; pcre:"/pagina=[^&]*\x27/Ui";
      metadata:service http; 
      reference:url,github.com/BuddhaLabs/PacketStorm-Exploits/blob/master/1309-exploits/pkcms-sql.txt;
      classtype:web-application-attack;
      sid:32768;
      rev:1;)
  ```

action - alert
protocol - tcp
source - external network
destination - internal netwok port 80
meaning - makes an alert if specific sql injection is attempted

**Follow Up Questions:** Based on the reference URL, which exploit does this rule monitor for?

**Follow Up Questions:** Based on your knowledge of SQL injection and the rule above, which of the following carries the SQLi payload? What is the name of the parameter or header that is being attacked?
  - POST data
  - Unsanitized HTTP header
  - GET query parameters)
