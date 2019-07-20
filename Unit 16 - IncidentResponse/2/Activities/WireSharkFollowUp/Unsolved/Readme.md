### Guided Practice: Wireshark Practice

- In this activity, you will work on investigating a malware attack using a snort alert file and a network pcap.

#### Setup

**Important**: This exercise uses live malware. Start with using your Ubuntu VM to work in a contained environment.

- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and/or malware analysis.
    - Author, Brad Duncan (2019). *Stormtheory* Retrieved from [https://www.malware-traffic-analysis.net/2019/02/23/index.html](https://malware-traffic-analysis.net/2019/02/23/index.html)

- Inside your VM, open the terminal and run `cd ~/Documents` to move to your documents folder.

- Run `mkdir alert` and `cd alert` to create and move into a working directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise.pcap.zip` and `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise-alerts.zip` to download the needed pcaps.

- Run `unzip '*.zip' && rm *.zip` to unzip the files.

- The password for these files is: 'infected'

#### Instructions

- In this exercise, you will locate and identify malware that has infected a host.

- You are provided with a snort alerts file, and a pcap file. For the snort files, you can use `grep` to search them or use `less` to read through them. You can also use Splunk to search them.

- There is a hints section at the bottom if you get stuck, and also a solutions file [HERE]() if you would prefer to work from the solutions.

- Start by examining the snort file, and answer these questions:
    - What activity is snort reporting on? (Provide a few alert headlines)
    - What is the date and time of this alert?
    - What is the external IP address that snort is flagging for malicious activity?
    - What is the internal IP address that snort is flagging for malicious activity?
    - What is the source port of the activity?
    - What is the destination port of the activity?

- Now, move into the pcap file.
    - Filter the pcap file to show you the conversation between the two machines that were identified in the snort alert.
    - What are the MAC Addresses of the computers involved?
    - What is the host name of the internal machine?
    - Can you confirm the date and time this issue occurred?
    - How can you confirm if the snort alert is accurate?
    - Can you safely verify whether or not malware was downloaded?
    - Would you categorize this alert as a `False Positive` or a `True Positive`?
    - If this issue needs to be mitigated, what steps should be taken with the infected machine?
    - What steps should be taken in regards to network security?
    - Would you categorize this issue as a Web, Email or Network attack?

#### HINTS SECTION

- If you need some hints to answer some of the questions above, you can use this section.

##### Snort Alert HINTS

- Try opening the snort alerts file with `less alerts_file.txt`
- Pay attention to the second line of each alert for hints about what happened.
- The third line of an alert gives you IP address traffic flow
- The fifth line of an alert gives you the port information

##### PCAP / Wireshark Alert HINTS

- Remember that most downloads are going to be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.
- Don't forget you can chain filters together with `and`, `or` and the like.
- If you find an interesting packet, right click and `Follow > TCP/UDP Stream` for more info.
- You also might find interesting info in `File > Export Objects > HTTP`
- Command line tools like `file` and `md5sum` will help too.
- Want to see if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload)
