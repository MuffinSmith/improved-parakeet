# Malicious Activity Solution File

## Solutions

- Open `aurora.pcapng`.

- What is the name of the first resource the client requests from the server?
  
   **Solution**: First, filter for `http`. Note that the first packet is a `GET` request for`/info`. 

- What is the server's response code for this request? What is the value of the `Location` header in that request?
   
   **Solution**: The server responds with a `302 Moved` response. The `Location` header contains the value `/info?rFfWELUjLJHpP—note the added query string.

- Do you notice anything suspicious about the server's response?
   
   **Solution**: The query string is suspicious because of the strange query string. It looks like a command and control message.

- Does it look anything like the HTML you've seen so far? Can you figure out anything about what the code means?
    
   **Solution**: Not much...One thing you can tell is that this is JavaScript, because it's code contained in a `<script>` tag. It's obfuscated, meaning the code is purposefully uninformative—you can tell because the first variable name is `IwpVuiFqihVySoJStwXmT`. Its value looks like a hex-encoded string (but hex decoding doesn't reveal much...Bummer). Towards the very bottom, there are some regular expression replacements and a call to `eval`, likely intended to de-obfuscate the JavaScript and execute the result.

- Immediately after receiving the HTML you just read, the browser sends a request for another file. What is the name of this file?
  
   **Solution**: The GIF is named `infowTVeeGDYJWNfsrdrvXiYApnuPoCMjRrSZuKtbVgwuZCXwxKjtEclbPuJPPctcflhsttMRrSyxl.gif`.

- Click on the response to highlight the response packet in the main Wireshark window. It should be packet 23.

- Return to the main Wireshark window. Look at the source/destination addresses for packet 23 and packet 24. What do you notice? Explain what happened with packet 24.
  
   **Solution**: Note that Packet 23 has `src` and `dst` addresses of `192.168.100.202` and `192.168.0.206`, respectively. Packet 24 has these addresses reversed. This indicates that `192.168.0.206` is opening a connection to `192.168.0.202`.

- Look at packet 25. What kind of data got sent?
  
   **Solution**: Note that these packets follow another TCP handshake between the client and server. If you right-click and select **Follow**->**Stream**, you'll see that a payload got sent over the wire—followed by a Windows Shell opened by the Aurora exploit!
  
Take a moment to address remaining questions before proceeding.
