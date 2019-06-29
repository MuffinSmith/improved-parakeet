# Attack Analysis

## Instructions
- Launch Wireshark and open the capture file in []().

- Answer the questions below.
  - What kind of attack is this?
  > **Solution**: This is a SQL injection attack.
  - How many bytes were transferred during the attack?
  > **Solution**: 7,098 bytes were transferred over IPv4. Note this by clicking **Endpoints**->**Statistics**.
  - What was the attacker's IP address? Their MAC address?
  > **Solution** IP address was `10.2.2.101`. Their MAC address was `c4:b3:01:bc:95:63`. Note this by clicking any of the incoming HTTP packets, and inspecting the **Internet Protocol** panel.
  - Did any of the attacks succeed? If so, what type of injection was it? 
  > **Solution**: Yes; filter for `tcp.stream eq 0`. This stream contains a successful UNION injection.
