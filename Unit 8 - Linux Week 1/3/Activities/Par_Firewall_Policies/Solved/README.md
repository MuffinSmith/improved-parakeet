# Firewall Policies

In this exercise, you'll work with a partner to design and implement a firewall policy. You will:
- Audit the services each machine furnishes
- Determine which ports should be exposed
- Design and document a firewall policy for each machine
- Implement the policy on each machine

The goal of this activity is to expose you to the full process around developing access control policies—from determining what should be available, to implementing controls that expose only these precise resources.

**Good luck!**

## Instructions

### Auditing

Review the list below, and fill out the blanks.

**Note**: An "API" is simply a way to retrieve information from a database via HTTP. In addition, you'll need to research the default port that MySQL binds.

- Service-Level Agreements for Supercorp's Intranet
  - User Data API
    - **Description**: Web server that provides access to organization's IAM database.
    - **Service(s)**: HTTP, HTTPS
    - **Port(s)**: 80, 443
  - User Database
    - **Description**: MySQL server containing user data for IAM policies. Should _only_ be accessible by the User Data API server.
    - **Service(s)**: MySQL
    - **Port(s)**: 3306
  - Command Server
    - **Description**: Server responsible for controlling whether other servers on the network are up or down. Allows administrators to log in remotely to issue commands. Block all requests to the telnet server that _do not_ come from the local subnet. Allow outgoing SSH and telnet connections to other machines within the subnet.
    - **Service(s)**: SSH, Telnet
    - **Port(s)**: 22, 23

### Implementing Access Controls

Refer to these UFW documents.
  - Common Firewall Rules and Commands: <https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands>
  - How to Setup a Firewall with UFW: <https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server>

- Begin by attaching to the scanner and using NMap to port-scan the subnet. Save the results in `/tmp/start_profile.benchmark`.

- Attach to each machine in the above list, and retrieve its IP Address. Document this for the steps below.

- Implement the policy above by attaching to each machine and using `ufw` to set the appropriate rules on each machine. For each, do the following:
  - Enable and start UFW.
    - **Solution**: `ufw enable && ufw start`. Enabling tells the machine to launch the firewall on startup, but doesn't actually activate it. `start` tells the machine to run the firewall, but does _not_ start it on boot.
  - Set a default rule to deny all incoming and outgoing traffic.
    - **Solution**
      - `ufw default deny incoming`
      - `ufw default deny outgoing`
  - Create rules exposing the ports you identified above.
    - **Solution**: This is different for each machine, but, as an example, the command server machine should have:
      - `ufw allow from 172.17.0.0/24 to any port 22`
      - `ufw allow from 172.17.0.0/24 to any port 23`
      - `ufw allow out to 172.17.0.0/24 port 22`
  - Save each machine's configuration in a file called: `/tmp/<machine_name>.policy`.
    - **Solution**: `ufw status verbose > /tmp/<machine_name>.policy`

### Generating Documentation

- Finally, create and move into a directory called `Policies`, and transfer the policy files you created in the step above to this directory.
