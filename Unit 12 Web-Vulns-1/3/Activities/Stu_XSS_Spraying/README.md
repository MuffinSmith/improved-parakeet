# XSS Injection Spraying

## Instructions

### XSS Spraying without Filters

- Navigate to tab `DVWA Security`, and set your security level to **Low**.

- In Burp, turn on the Interceptor.

- Navigate to `XSS (Reflected)`, and send the intercepted request to Intruder.

- Use Intruder on Burp Suite to send the payloads in `xss_payloads.txt` to the web form. Pause the attack after 50 injections are used. 
  
- Review 5-10 of the responses to your attack. 
  - Can you identify any pages in which the payload was echoed without escaping? 
  - Can you demonstrate that this payload actually results in JavaScript execution on the client?

- Keep track of the XSS payloads that were successful. You'll need them for the next exercise.

### XSS Spraying Against Filters

- Navigate to tab `DVWA Security`, and set your security level to **High**.

- Run your XSS spray again. Which payloads work this time?

### Questions

- List three ways a web developer could protect their web application from XSS attacks.
