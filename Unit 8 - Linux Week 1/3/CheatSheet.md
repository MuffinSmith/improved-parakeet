# Day 3 Cheat Sheet — Introduction to Linux
## Key Terms

- **SOHO**: Small Office Home Office Network
  > **Example**: Refers to most small LAN Networks.

- **Physical Network Connection**: The physical medium.
  > **Example**: Wires, Wireless Media Devices, Etc.

- **Logical Network Connection**: The abstract path data takes in order to arrive from Point A to Point B.
  > **Example**: When you connect to Google.com, your computer is making a logical connection to Google's servers.

- **Packet**: A small chunk of data to be moved across a network.
  > **Example**: All data traveling across a network is first broken into many small packages before it's transmitted.

- **IP Address**: Internet Protocol Address
  > **Example**: A logical address that identifies a host on a network. An IP address is assigned to every device on a network. It is analogous to a device's street address where other computers can contact it.

- **MAC Address**:  Media Access Control Address
  > **Example**: A MAC address is A unique hardware identifier for a network interface, assigned by the hardware manufacturer.

- **NIC**: Network Interface Controller
  > **Example**: Network Interface Controllers (NICs) describe computer hardware that connects a computer to a computer network. Every NIC is assigned a MAC address, printed on the device at the time of manufacturing.

- **Gateway**: A device that acts like a "go-between" for devices on a LAN and devices on the public internet.
  > **Example**: Your home router is one such gateway.

- **Router**: A networking device that forwards data packets between computer networks.
  > **Example**: The simplest routers forward IP packets between home computers and the web.

- **Switch**: Network switches are computer networking devices that connect multiple devices together.
  > **Example**: Switches create networks. Typically you will see switches feed into Routers.

- **Bridge**: Bridges are effectively switches but with only two ports available.
  > **Example**: Bridges are often used to tie two LANs together.

- **Hub**: Network Hubs are an older version of switches, but unlike Switches – hubs cannot differentiate between each device on the network.
  > **Example**: Hubs rely on constantly broadcasting communication to all devices.

- **Wireless Access Point**: A Wireless Access Point (WAP) is a network hardware device that allows a Wi-Fi device to connect to a wired network.
  > **Example**: Increasingly WAPs are built into routers as in the case of all-in-one devices most consumers use in their home.

- **Modem**: **Mo**dulator - **Dem**odulator
  > **Example**: Modems convert digital information for transmission and converts transmitted information back into digital information.

- **Firewall**: Firewalls filter data entering or exiting a network.
  > **Example**: A firewall can refer to software running on your computer (Host-based) OR a hardware device that monitors network traffic (Network-based).

- **Load Balancing**: A device that will redirect traffic to a backup server, or between multiple servers, depending on network traffic.
  > **Example**: One use of load balancing is to keep a website active by balancing heavy internet traffic between multiple web servers. Without load balancing, a server may stop responding if too many users are accessing it at one time.

- **Network Topology**: The arrangement of devices and connections on a network.
  > **Example**: One of the main reasons that topology matters for security is that it determines which devices are connected to which. Different arrangements of devices have advantages/disadvantages regarding redundancy, bandwidth usage, and latency.

- **Network Architecture**: The deliberate design of devices and connections on a network.
  > **Example**: As security professionals, _architecture_ is the exercise of ensuring that the network's topology ensures CIA.

- **Ring Topology**: In a ring topology, each device is connected to the next device in the chain.
  > **Example**: Simple to build and doesn't require a central node (e.g., switch; router) but if any one device goes down, the entire network is affected.

- **Dual Ring Topology**: A Dual Ring Topology is a Ring Topology, but with _two_ rings of data links, rather than one.
  > **Example**: This is the same as a Ring Topology, but if any link in one of the rings fails, the link from the second ring will compensate.

- **Linear Topology**: In a linear topology, each device is connected to the adjacent device via a two-way link. The two devices at the "ends" of the network are _not_ connected to one another, by contrast to a ring topology.
  > **Example**: Adding devices to the network is easy but a single device failure can interrupt the entire network.

- **Star Topology**: In a star topology, all devices in the network are attached to a central node (usually a switch or a router). Devices transmit data by sending it to the central node, which then determines which other device on the network to forward it to.
  > **Example**: Failure of an end device doesn't endanger the entire network, but the number of devices on the network is constrained by the number of ports available on the central node.

- **Bus Topology**: In a Bus Topology, every device is attached to a central data link.
  > **Example**: Data transmission is fast between all devices and it's easy to expand the network but two devices cannot transmit data simultaneously and sending the data to every device on the network wastes bandwidth.

- **Mesh Topology**: Also known as a 'Partial Mesh Topology', this is like a Full Mesh Topology, but not _every_ pair of devices is directly connected.
  > **Example**: Devices on the network cooperate to find the shortest path to forward data to one another over.

- **Full Mesh Topology**: In a Full Mesh Topology, every device on the network is directly connected to every other.
  > **Example**: Highly redundant—if a single link between devices fails, both devices can still communicate with the rest of the network, but it is very complicated to set up and manage.

- **Tree Topology**: Also known as a 'Star-bus' Topology, a Tree Topology is a Hybrid network combination of the Star and Bus topologies.
  > **Example**: Multiple Star topologies are connected to a primary data link.

- **Hybrid Topology**: A Hybrid Topology is any combination of the above topologies. e.g., a Linear Topology with Star Networks attacked to the endpoints.
  > **Example**: Most modern networks are Hybrid Topologies.

- **IDS**: Intrusion Detection System
  > **Example**: Usually a combination of software and hardware that that monitors network traffic for malicious activity or security policy violations. 'Snort' is an example of a widely used IDS.

- **IAM**: Identity and Access Management.
  > **Example**: IAM Systems store identity information used for authentication and information about which resources a user is authorized to access. Controls who can modify what data on what system.

## Key Commands

### Tcpdump

`tcpdump` is functionally similar to Wireshark, in that it captures packets from the NIC. The fundamental difference is that `tcpdump` is launched on the command-line, and provides no graphical interface.

```bash
# Capture icmp packets with source/destination IP addresses on all network interfaces.
tcpdump -i any -n -s 0 icmp
```

`tcpdump` also allows users to save PCAP files using a command-line flag.

```bash
# Capture icmp packets with source/destination IP addresses on all network interfaces.
tcpdump -i any -n -s 0 icmp -w my_capture.pcap
```

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-i any</code> instructs `tcpdump` to listen on all interfaces.
    <li><code>-n</code> directs `tcpdump` to skip name resolution—in other words, packets will contain IP Addresses instead of host names in their Source/Destination attributes.
    <li><code>-s 0</code> ensures `tcpdump` captures every packet in full, as opposed to just the first 96 bytes (the default).
    <li><code>icmp</code> specifies the type of packet you are listening for.
    <li><code>-w <my_capture.pcap></code> writes the capture to a file named 'my_capture.pcap'.
  </ul>
</details>

#### ufw

`ufw` is a firewall configuration utility found on many Linux machines. Using it, you can easily deny incoming packets based on certain conditions, such as source IP; malformed TCP flags; etc.

```bash
# Allow a specific host from IP address '172.17.0.9' to access this machine.
ufw allow from 172.17.0.9 to any
```

```bash
# Deny all traffic using a specific port.
ufw deny 80
```
In this case we are denying all traffic to port 80.

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>enable</code> starts up the ufw firewall service.
    <li><code>disable</code> stops the firewall service.
    <li><code>reload</code> reloads the firewall rules (after changes are made).
    <li><code>-to any</code> allows access to _any_ port on the host.
    <li><code>allow</code> creates an allow/whitelist rule.
    <li><code>deny</code> creates a deny/blacklist rule.
    <li><code>status numbered</code> shows a list of firewall rules numbered in order of execution.
    <li><code>insert <number></code> inserts a rule to a specific location in the list.
    <li><code>delete <number></code> deletes a specific rule by it's number in the list.
  </ul>
</details>
