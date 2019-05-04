# Firewall Policies

In this exercise, you'll work with a partner to design and implement a firewall policy. You will:
- Audit the services each machine furnishes
- Determine which ports should be exposed
- Design and document a firewall policy for each machine
- Implement the policy on each machine

The goal of this activity is to expose you to the full process around developing access control policies—from determining what should be available, to implementing controls that expose only these precise resources.

## Instructions

### Auditing

Review the list below, and fill out the blanks.

**Note**: An "API" is simply a way to retrieve information from a database via HTTP. In addition, you'll need to research the default port that MySQL binds.

- Service-Level Agreements for Supercorp's Intranet
  - User Data API
    - **Description**: Web server that provides access to organization's IAM database. This machine runs an HTTP and HTTPS server, which should be available to all machines on the subnet. There is also an SSH listener, which should only allow access from the command server. Disable connections to all other running services.
    - **Service(s)**: TODO
    - **Port(s)**: TODO
  - User Database
    - **Description**: MySQL server containing user data for IAM policies. Should _only_ be accessible by the User Data API erver.
    - **Service(s)**: TODO
    - **Port(s)**: TODO
  - Command Server
    - **Description**: Server responsible for controlling whether other servers on the network are up or down. Allows administrators to log in remotely to issue commands. Block all requests to the telnet server that _do not_ come from the local subnet. Allow outgoing SSH and telnet connections to other machines within the subnet.
    - **Service(s)**: TODO
    - **Port(s)**: TODO

### Generating Documentation

- Finally, create and move into a directory called `Policies`, and copy over the policy files and benchmark you created.
