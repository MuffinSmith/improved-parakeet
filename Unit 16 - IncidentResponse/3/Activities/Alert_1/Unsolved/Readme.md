### Guided Practice: !Alert 1! (0:30)

- In this activity, you will investigate a malware attack using a Snort alert file and a network pcap.

#### Setup

- **Important**: All of today's exercises use live malware. Use your Ubuntu VM to work in a contained environment.

- We will use exercise files from [malware-traffic-analysis.net]. This site provides many open-source malware pcap files and activities for anyone to access and to use for practicing incident response and malware analysis.
    
    - Author, Brad Duncan (2019). *Timbershade* Retrieved from [https://malware-traffic-analysis.net/2019/01/28/index.html](https://malware-traffic-analysis.net/2019/01/28/index.html)

- You may find it easiest to setup Slack on your VM, so you can access activities and links directly on your VM.

- Inside your VM, open the terminal and run `cd ~/Documents` to move to your documents folder.

- Run `mkdir alert_1` and `cd alert_1` to create and move into a working directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2019/01/28/2019-01-28-traffic-analysis-exercise.pcap.zip` and `wget https://malware-traffic-analysis.net/2019/01/28/2019-01-28-alerts-for-traffic-analysis-exercise.txt.zip` to download the required files.

- Run `unzip '*.zip' && rm *.zip` to unzip the files. The password for these files is: `infected`

#### Instructions

- In this exercise, you will work from an alert file and determine if the alert is a `False Positive` or a `True Positive`

- You are provided with a Snort alerts file and a pcap file.

- There is a Hints section at the bottom of this file in case you get stuck. Also, a solutions file [here](Activities/Alert_1/Solved/Readme.md) if you would prefer to work backwards from the solutions.

- Begin by examining the Snort file and answer these questions:
    
    - What activity is Snort reporting on? (Provide a few alert headlines.)
    
    - What is the date and time of this alert?
    
    - What is the external IP address that Snort is flagging for malicious activity?
    
    - What is the internal IP address that Snort is flagging for malicious activity?
    
    - What is the source port of the activity?
    
    - What is the destination port of the activity?

- Now, move into the pcap file.
    
    - What is the MAC Address of the internal computer involved?
    
    - What is the host name of the internal machine?
    
    - Can you confirm the date and time this issue occurred?
    
    - How can you confirm if the Snort alert is accurate?
    
    - Can you safely verify whether or not malware was downloaded?
    
    - Would you categorize this alert as a `False Positive` or a `True Positive`?
    
    - If this issue needs to be mitigated, what steps should be taken with the infected machine?
    
    - What steps should be taken in regards to network security?
    
    - Would you categorize this issue as a Web, Email or Network attack?

#### Hints: 

If you need some hints, you can use this section. 

##### Snort Alert Hints

- Try opening the snort alerts file with `less alerts_file.txt` or open it with Splunk.

- Pay attention to the second line of each alert for clues about what happened.

- The third line of an alert gives you IP address traffic flow.

- The fifth line of an alert gives you the port information.

##### PCAP / Wireshark Alert Hints

- Remember that most downloads are going to be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.

- Don't forget you can chain filters together with `and`, `or` and the like.

- If you find an interesting packet, right click and `Follow > TCP/UDP Stream` for more info.

- You also might find interesting info in `File > Export Objects > HTTP`

- Command line tools like `file` and `md5sum` will help too.

- Want to see if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload).