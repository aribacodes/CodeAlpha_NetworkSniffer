 CodeAlpha Task 1: Basic Network Sniffer

###  Intern: **Ariba Abbasi**
###  Internship Domain: Cyber Security  
###  Organization: [CodeAlpha](https://www.codealpha.tech)  
###  Task Name: Basic Network Sniffer  
###  Tools Used: Python, Scapy, Colorama 
GitHub: https://github.com/aribacodes
LinkedIn: www.linkedin.com/in/ariba-abbasi-936983360

....

##  Project Description

This project is a **Python-based network packet sniffer** developed as part of my cybersecurity internship at CodeAlpha.  
It uses the `scapy` library to capture and analyze real-time packets flowing through the network. The output is displayed in a **readable, color-coded format**, showing key details like:

-  Packet number  
-  Timestamp  
-  Source IP  
-  Destination IP  
-  Protocol used  
-  Packet summary

This sniffer is helpful for understanding **how data flows in a network**, and forms a foundational concept in **network security**, **threat detection**, and **ethical hacking**.

....

##  Features

- Real-time network packet capture
- Limit of 20 packets for demo control
- Clear terminal output using Colorama
- Shows summary of each packet captured
- Easy to use, well-documented code

....

##  Installation

> You must have Python installed on your system.  
> Use `pip` to install required libraries:

```bash
pip install scapy colorama

....

##  **How to Run the Code**

### Step 1: Install the required library
```bash
pip install scapy
```

### Step 2: Run the script
```bash
python sniffer.py
```


....

##  Sample Output

Packet #1 at 2025-07-02 23:08:48
     From: 40.79.189.59
     To:   192.168.1.7
     Protocol: 6
     Summary: Ether / IP / TCP 40.79.189.59:https > 192.168.1.7:50017 SA

 Packet #2 at 2025-07-02 23:08:48
     From: 192.168.1.7
     To:   40.79.189.59
     Protocol: 6
     Summary: Ether / IP / TCP 192.168.1.7:50017 > 40.79.189.59:https 

##  Task Status
Completed and Submitted 


