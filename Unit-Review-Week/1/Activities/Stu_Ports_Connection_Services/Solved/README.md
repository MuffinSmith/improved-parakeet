#  Ports, Connections, and Services

## Instructions

### Services
- Define "service".
  - Put differently: What is the main purpose of a service?
  > **Solution**: A _service_ is a process that listens for requests from other machines. An example would be the Apache HTTP server, which listens for HTTP requests. When a server receives a request, it sends a _response_. This model is called **client-server architecture**, and is the underlying architecture of the Internet.

### Ports
- What is the relationship between ports and services?
  > **Solutions**: Services are processes running on a host. Ports are essentially "names"/"addresses" for those processes that are visible to other machines.

- What is the relationship between ports and IP addresses?
  > **Solutions**: IP addresses specify a computer on the network. Port numbers specify a process on that host. IP addresses and port numbers are used in concert to specify a service running on a host on a network.

- Write down the port typically used by each service below.
  - FTP: 22
  - NetBIOS: 445
  - MS-SQL: 1433
  - MySQL: 3306
  - SSH: 22
  - SMTP: 25
  - DNS: 53/udp
  - HTTP: 80
  - HTTPS: 443
  - SMB: 139

### Connections
- What is the difference between "connection-oriented" and "connectionless" protocols?
  > **Solution**: Connection-oriented protocols establish "connections" between hosts, which ensure error handling in the event of poor transmission; graceful teardown, etc. Connectionless protocols simply send data, without paying attention to whether it arrived safely.

- Name three advantages of connection-oriented protocols.
  > **Solution**: Error handling; graceful teardown; guaranteed delivery.

- Describe the TCP 3 Way Handshake.
  - Why is the handshake "3-way"?
  - Which TCP flags do the client/server set?
    - **Solution**: The handshake involves the exchange of three packets: A SYN Packet sent from the client initiating the connection; a SYN/ACK response from the server; and an ACK response from the client.

- Suppose you're streaming video over a TCP connection. 
  - What happens when packets get dropped?
    > **Solution**: The client re-requests the dropped packet, and reassembles everything in the proper order after receiving it.
  - What happens when packets get dropped over a UDP connection?
    > **Solution**: Nothing; the client simply doesn't receive the packet, nor know it was dropped.
  - Would you prefer to use UDP or TCP for video streaming? Why?
    > **Solution**: In practice, UDP is often used, because occasional dropped packets don't dramatically affect frame rates.

- What is a "keepalive" connection? Why is it more efficient than a "close" connection?
  > **Solution**: A keepalive connection is a TCP connection used for _multiple_ HTTP requests. A "close" connection is alive for only a _single_ HTTP request.
