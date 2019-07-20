### Guided Practice: !Alert 2! (0:30)

- In this activity, you will investigate two alert files along with a pcap and three emails to determine if the alerts are a `false positive` or a `true positive`.

#### Setup

**Important**: This exercise uses live malware. Start with using your Ubuntu VM to work in a contained environment.


- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and/or malware analysis.

   - Author, Brad Duncan (2019). *Sputnik House* Retrieved from [https://malware-traffic-analysis.net/2018/08/12/index.html](https://malware-traffic-analysis.net/2018/08/12/index.html)

- Inside your VM, move to your documents folder and create an `alert_2` directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2018/08/12/2018-08-12-traffic-analysis-exercise.pcap.zip`, `wget https://malware-traffic-analysis.net/2018/08/12/2018-08-12-traffic-analysis-exercise-emails.zip` and `wget https://malware-traffic-analysis.net/2018/08/12/2018-08-12-traffic-analysis-exercise-alerts.zip` to download the needed files.

- Unzip the files.

- The password for these files is: `infected`

#### Instructions

- You are provided with a Snort alerts file, a Suricata alerts file, two emails and a pcap file.

- There is a hints section at the bottom if you get stuck. Also, a solutions file found [here](Activities/Alert_2/Solved/Readme.md) if you would prefer to work backwards from the solutions.

- Start by answering these questions:

   - What activity is snort reporting on? (Provide a few alert headlines)

   - What is the date and time of this alert?

   - What is the external IP address that snort is flagging for malicious activity?

   - What is the internal IP address that snort is flagging for malicious activity?

   - What is the source port of the activity?

   - What is the destination port of the activity?

- Now answer these questions:

    - What is the MAC Address of the internal computer involved?

    - What is the host name of the internal machine?

    - Can you confirm the date and time this issue occurred?

    - How can you confirm if the snort alert is accurate?

    - Can you safely verify whether or not malware was downloaded?

    - Can you determine which email had a malware attachment related to the Snort Alerts?

    - Would you categorize this alert as a `False Positive` or a `True Positive`?

    - If this issue needs to be mitigated, what steps should be taken with the infected machine?

    - What steps should be taken in regards to network security?

    - Would you categorize this issue as a Web, Email or Network attack?

#### Hints:

Use this section if you need any hints to answer the questions above.

##### Snort Alert Hints

- Try opening the Snort alerts file with `less alerts_file.txt` or use Splunk.

- Pay attention to the second line of each alert for clue about what happened.

- The third line of an alert gives you IP address traffic flow.

- The fifth line of an alert gives you the port information.

##### PCAP / Wireshark Alert HINTS

- Remember that most downloads will be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.

- Don't forget you can chain filters together with `and`, `or` and the like.

- If you find an interesting packet, right click and `Follow > TCP/UDP Stream` for more info.

- You also might find interesting info in `File > Export Objects > HTTP`

- Want to see if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload)

##### Email Hints

- You can safely view these emails using a mail program like 'Thunderbird' or you can also use `Less` and `VIM` to view them.

- These emails have attachments that you will want to extract and examine.

- Command line tools like `file` and `md5sum` will be helpful too.
