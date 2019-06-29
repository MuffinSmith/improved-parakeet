# Replaying Requests with Repeater

In this exercise, you'll practice
- Using Burp Repeater to resend requests with different parameters
- Manipulating cookies to change an application's behavior

## Instructions

- Navigate to any vulnerability in DVWA.

- Turn on Burp Interceptor, and reload the page. Inspect the intercepted request.
  - Which cookies do you see?

- Send the intercepted request to Repeater. Then, forward it as-is. 

- Inspect the response. What is the **Security Level** of DVWA, based on the response?

- Use Repeater to set the security level to `impossible`, and use the response to determine if your "hack" was successful.
