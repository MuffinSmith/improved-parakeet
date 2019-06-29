# XSS Injection Spraying

## Instructions

### XSS Spraying without Filters

- Navigate to `192.168.99.100/security.php`, and set your security level to **Low**.

- In Burp, turn on the Interceptor.

- Navigate to `192.168.99.100/vulnerabilities/xss_r`, and send the intercepted request to Intruder.

- Use Intruder to send the payloads in `xss_payloads.txt` to the web form.
  
- Review the responses to your attack. 
  - Can you identify any pages in which the payload was echoed without escaping? 
  - Can you demonstrate that this payload actually results in JavaScript execution on the client?

- Keep track of the XSS payloads that were successful. You'll need them for the next exercise.

### XSS Spraying against Filters

- Navigate to `192.168.99.100/security.php`, and set your security level to **High**.

- Run your XSS spray again. Which payloads work this time?
