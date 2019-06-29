# Webshell Recon
For this exercise, you'll perform some recon on the server you compromised in the previous class.

Use Firefox to navigate to: <http://ptl-f99df351-3bdd4c8f.libcurl.so/admin/index.php>

Then, follow the instructions below.

## Instructions

- Upload [webshell.php](webshell.php) to the server.

- Launch Burp Suite, and intercept a request the URL where `webshell.php` was uploaded.

- Send the request to Intruder. Set a position around the command in the request, and send payloads that will dump the following information:
  - The current user ID and group ID
  - A list of running processes running as root
  - The contents of `/etc/passwd`
  - Check if the following network tools are installed:
    - `nc`
    - `ncat`
    - `socat`
    - `curl`
    - `wget`
    - **Hint**: To check if a tool exists, check for its version with, e.g.: `nc --version`.

- Read the following Server Fault thread: <https://serverfault.com/questions/519215/what-is-the-difference-between-sbin-nologin-and-bin-false>

- Based on your research and findings: Can you use your webshell, which runs commands one at a time, to get an _interactive_ shell on the server? Why or why not?
  - **Note**: Consider who your current user is and the contents of `/etc/passwd`.
