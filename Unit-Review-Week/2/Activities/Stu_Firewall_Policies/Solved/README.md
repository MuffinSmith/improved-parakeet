# Firewall Policies Solution Guide:

### Part 1: Auditing

Review the list below, and fill out the blanks.

**Note**: An "API" is simply a way to retrieve information from a database via HTTP. In addition, you'll need to research the default port that MySQL binds.

#### Service-Level Agreements for Supercorp's Intranet
  
  - User Data API (`192.168.12.50`)
    - **Description**: Web server that provides access to organization's IAM database. This machine runs an HTTP and HTTPS server, which should be available to all machines on the subnet. There is also an SSH listener, which should only allow access from the command server. Disable connections to all other running services.
    - **Service(s)**: HTTP, HTTPS
    - **Port(s)**: 22, 80, 443
  
  - User Database (`192.168.12.75`)
    - **Description**: MySQL server containing user data for IAM policies. Should _only_ be accessible by the User Data API server.
    - **Service(s)**: MySQL
    - **Port(s)**: 3306
  
  - Command Server (`192.168.12.100`)
    - **Description**: Server responsible for controlling whether other servers on the network are up or down. Allows administrators to log in remotely to issue commands. Block all requests to the telnet server that _do not_ come from the local subnet. Allow outgoing SSH and telnet connections to other machines within the subnet.
    - **Service(s)**: SSH, Telnet
    - **Port(s)**: 22, 23
    



### Part 2: Generating Documentation
- Create a directory to save firewall information in: `~/security/firewall_policies`. Move into this directory.
- Create a new file for each machine—e.g., `command_server.ufw.rules`.
- Write the UFW commands you would run to implement the correct firewall rules in each file.

  ```bash
  # api_server.ufw.rules
  sudo ufw allow from 192.168.12.100 to any port 22
  sudo ufw allow from 192.168.12.0/24 to any port 80
  sudo ufw allow from 192.168.12.0/24 to any port 443
  ```
  
  ```bash
  # command_server.ufw.rules
  sudo ufw allow from 192.168.12.0/24 to any port 22
  sudo ufw allow from 192.168.12.0/24 to any port 23
  ```
  
  ```bash
  # userdb.ufw.rules
  sudo ufw allow from 192.168.12.50 to any port 3360
  ```

Answer any questions before moving on. 
