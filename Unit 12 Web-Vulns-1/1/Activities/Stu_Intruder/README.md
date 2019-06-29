# Brute Force Intrusion

In this exercise, you'll get your feet wet with Intruder by automating the manual research you did in the previous exercise.

## Instructions

### Scripting Requests

- Return to `192.168.99.100/vulnerabilities/exec`, and turn on the Interceptor in Burp Suite.

- Submit a command injection, and send the request to Intruder.

- Use Intruder to determine which of the following languages is installed on the target server:
  - Python
  - Ruby
  - Perl
  - Java
  - PHP

- Use Intruder to determine which of the following tools is installed on the target server:
  - ncat
  - nc
  - wget
  - curl
  - socat
  
## Hints

- To determine which languages are installed on the target, use the same command injection you developed previously, but parameterize the _language_.

- To determine which tools are installed on the target, use the same command injection you developed previously, but parameterize the _tool name_.
