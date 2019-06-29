# OWASP Top 10 - A Primer
This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities
### A3:2017 - Sensitive Data Exposure
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of sensitive data exposure
 - What kind of damage it can do to a business

#### How it Works
TODO: Define **Local File Inclusion (LFI)**, and explain why it's an example of a Sensitive Data Exposure vulnerability.

#### Scenario
TODO: Explain the LFI vulnerability you explored on the DVWA **File Inclusion** page.

Specifically, explain
- How you perform the attack
  - **Note**: Include the URL you use to demonstrate the LFI, and provide a screenshot of the output it generates.
- Why the attack works
- How the server could be configured to prevent this attack
---
### A4:2017 - XML External Entities (XXE)
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of XXE attacks
 - What kind of damage it can do to a business

#### How it Works
TODO: Explain the following:
  - What XML is
  - How web applications use XML
  - Why web applications can be attacked via XML uploads
  - Ways that XXE payloads can be delivered

#### Scenario
TODO: Use your knowledge of command injections to explain what each of the following XXE payloads does.

##### Payload 1
```xml
<?xml version="1.0" encoding="ISO-8859-1"?> <!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]> <foo>&xxe;</foo>
 ```
 TODO: Explain what this payload is used for, and identify which other OWASP vulnerability is relevant.
 
 ##### Payload 2
```xml
<!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>
 ```
 TODO: Explain what this payload is used for, and identify which other OWASP vulnerability is relevant.

##### Payload 3
```xml
<!ENTITY xxe SYSTEM "file:///dev/random" >]>
 ```

TODO: Explain why this payload attempts to download an endless file.

---
### A5:2017 - Broken Access Control
#### Definition / Description
TODO: Use the OWASP document to explain
- The source, scope, and severity of broken access control vulnerabilities
 - What kind of damage it can do to a business

#### How it Works
TODO: Explain why LFI also qualifies as a Broken Access Control vulnerability!

#### Scenario
Suppose you log into an application as the user `jane`, and get redirected to: `https://example.site/userProfile.php?user=jane`.

Suppose Jane is able to see Bob's profile by navigating to: `https://example.site/userProfile.php?user=bob`
- This is called **Insecure Direct Object Reference (IDOR)** Read about it here: <https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)>.
---
### A7:2017 - Cross-Site Scripting (XSS)
#### Definition / Description
TODO: Use the OWASP document to explain
- The source, scope, and severity of XSS vulnerabilities
- The three different classes of XSS vulnerabilities
- What kinds of attacks can be carried out with XSS
 
#### How it Works
TODO: Explain how a reflected XSS payload gets echoed from an HTTP request to an HTML document.

#### Scenario
TODO: Explain how the reflected XSS on DVWA works. Exploit it with Burp Repeater, and include the HTTP request containing your payload below.

```
# HTTP Request w/ Reflected XSS Payload Here
```

### A8:2017 - Insecure Deserialization
#### Definition / Description
TODO: Use the OWASP document and this [Acutenix article](https://www.acunetix.com/blog/articles/what-is-insecure-deserialization/) to explain the following:
- What serialization is
- What deserialization is
- What web applications use serialization/deserialization for
- What kinds of attacks can be carried out by exploiting insecure deserialization bugs
- 
#### How it Works / Scenario
TODO: Explain how the exploit discussed in the Acutenix article achieves remote code execution (RCE). 

### A9:2017 - Using Components with Known Vulnerabilities
#### Definition / Description
TODO: Use the OWASP document to define the vulnerability.

#### How it Works
TODO: Use [this article](https://news.thomasnet.com/featured/new-nist-framework-focuses-on-supply-chain-security/) to explain supply chain risk in general.

#### Scenario
TODO: Read about the [leftpad incident](https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/), and discuss how this scenario almost seems like an accidental DoS attack.

### A10:2017 - Insufficient Logging & Monitoring
#### Definition / Description
TODO: Use the OWASP document to define the vulnerability.

#### How it Works / Scenario
TODO: Give an example scenario in which insufficient logging/monitoring hindered forensic or defensive efforts.
