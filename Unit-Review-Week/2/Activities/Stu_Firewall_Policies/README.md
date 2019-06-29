# Firewall Policies

In this exercise, you'll work with a partner to design and implement a firewall policy. You will:
- Audit the services each machine furnishes
- Determine which ports should be exposed
- Design and document a firewall policy for each machine

The goal of this activity is to expose you to the full process around developing access control policies: from determining what should be available, to implementing controls that expose only these precise resources.

**Good luck!**

**Good luck!**

## Instructions

### 1. Auditing

Review the machine descriptions below and fill in the "TODO" sections.

**Note**: An **API** is simply a way to retrieve information from a database via HTTP. You'll need to also research the default port that MySQL binds.

#### Service-Level Agreements for Supercorp's Intranet
  
  - User Data API (`192.168.12.50`)
    - **Description**: A web server that provides access to an organization's IAM database. This machine runs an HTTP and HTTPS server, which should be available to all machines on the subnet. There is also an SSH listener, which should only allow access from the command server. Disable connections to all other running services.
    - **Service(s)**: HTTP, HTTPS, SSH
    - **Port(s)**: 80, 443, 22
  
  - User Database (`192.168.12.75`)
    - **Description**: MySQL server containing user data for IAM policies. Should _only_ be accessible by the User Data API server.
    - **Service(s)**: MySQL
    - **Port(s)**: 3306
  
  - Command Server (`192.168.12.100`)
    - **Description**: Server responsible for controlling whether other servers on the network are up or down. Allows administrators to log in remotely to issue commands. Blocks all requests to the telnet server that _do not_ come from the local subnet. Allow outgoing SSH and telnet connections to other machines within the subnet.
    - **Service(s)**: SSH, Telnet
    - **Port(s)**: 22, 23

### 2. Generating Documentation

#### Complete the following supporting documentation:

- Create a directory to save firewall information in: `~/security/firewall_policies`. Move into this directory.
- Create a file to store firewall rules for each machine on the network—e.g., `command_server.ufw.rules`.
- Write the UFW commands you'd use to implement the access controls for each machine in their respective files.

```bash
// api_server.ufw.rules
sudo ufw allow from 192.168.12.0/24 to any port 80 //http
sudo ufw allow from 192.168.12.0/24 to any port 443 //https
sudo ufw allow from 192.168.12.100 to any port 22 //ssh 

// userdb.ufw.rules
sudo ufw allow from 192.168.12.50 to any port 3360

//command_server.ufw.rulessudo 
ufw allow from 192.168.12.0/24 to any port 22
ufw allow from 192.168.12.0/24 to any port 23
```