# Burp Repeater

## Instructions

### "Simple" Command Injection

- Navigate to `http://192.168.99.100/vulnerabilities/exec`, and turn the Interceptor off.

- Enter an IP address to ping, and observe the form's behavior.

- Turn on the Interceptor, and submit the form again. Send the intercepted request to Repeater.

- Use Repeater to ping a different IP address than before. When you've verified you can do this just fine, use command injection to perform the following tasks:
  - The username and user ID of the server processSQLi
    - **Solution**: `id`
  - The Operating System and Kernel Version of the server
    - 
  - Exfiltrate (read) the contents of `/etc/passwd`

### Bypassing Filters

- Navigate to `http://192.168.99.100/security.php`, and set your security level to **Medium**. In addition, **turn off Burp Suite's Interceptor**.

- Return to `http://192.168.99.100/vulnerabilities/exec`, and attempt the command injection you found earlier. It shouldn't work.

- Return to the vulnerable page, and turn the Interceptor back on. Submit a request, and send it to Repeater.

- Attempt to update your injection with the other metacharacters you've learned. Keep track of which ones work and which ones don't. You should find at least **two** methods to bypass the filter.

## Extension

- Attempt to read `/etc/shadow`. Describe the result, and explain why you think this happens.
  - _Prove_ your hypothesis by redirecting standard error to standard output.
    - **Hint**: For example: `less nonexistent.file 2>&1` prints the error message on the web page, but `less nonexistent.file` does not.

- Determine which of the following programming languages are installed on the server, and document your evidence in support/against each.
  - Python
  - Ruby
  - Perl

- Finally, determine if the following networking tools are installed on the server.
  - ncat
  - nc
  - wget
  - curl
  - socat

## Questions

- Suppose you've found `perl` and `socat` on the target server. Devise a strategy for opening a connection from the server to your attacking machine.

- Explain why the command injection starts to work after you use the `&` character. Be prepared to share your response with the class.