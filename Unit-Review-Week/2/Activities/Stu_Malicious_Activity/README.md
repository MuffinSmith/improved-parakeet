## Malicious Activity

When it comes to computer viruses, prevention is the best medicine. But it's hard to keep malware from getting in without knowing what it looks like. 

In this activity, you'll observe a computer getting hit with a sophisticated backdoor that gave hackers access to machines at Google, Adobe, and other companies back in 2009.

- You will continue investigating pcap files. 
- Even with NIDS like Snort, attackers can still find their way through the network and onto victims computers.
- You will be given a pcap file based involving an exploit called Aurora and are required to investigate the nature of the attack. 


### Instructions

- Open `aurora.pcapng`.

- What is the name of the first resource the client requests from the server?

- What is the server's response code for this request? What is the value of the `Location` header in that request?

- Do you notice anything suspicious about the server's response?

  - Does it look anything like the HTML you've seen so far? Can you figure out anything about what the code means?

- Immediately after receiving the HTML you just read, the browser sends a request for another file. What is the name of this file?

- Click on the response to highlight the response packet in the main Wireshark window. It should be packet 23.

- Return to the main Wireshark window. Look at the source/destination addresses for packet 23 and packet 24.

  - What do you notice? Explain what happened with packet 24.

- Look at packet 25.

  - Who's sending data to whom?

  - What kind of data got sent?
