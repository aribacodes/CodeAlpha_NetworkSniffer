
#Task 1: Basic Network Sniffer
#Author: Ariba Abbasi
#Internship: CodeAlpha Cyber Security
#Description: This script captures 20 network packets, displays key details such as source/destination IPs,
#protocol used, and packet summary. Uses Scapy for sniffing and Colorama for pretty output.


from scapy.all import sniff, IP                      #Import sniffing function and IP packet structure from Scapy
from datetime import datetime                        #For timestamping each packet
from colorama import Fore, Style, init               #For colored terminal output

#Initialize colorama for Windows compatibility
init()

#Counter for total packets processed
packet_count = 0

#Function to process each captured packet
def process_packet(packet):
    global packet_count
    packet_count += 1

    # Only process packets that have an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

        # Print formatted and colored output
        print(f"\n{Fore.CYAN} Packet #{packet_count} at {time_stamp}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}     From: {ip_layer.src}")
        print(f"     To:   {ip_layer.dst}")
        print(f"     Protocol: {ip_layer.proto}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}     Summary: {packet.summary()}{Style.RESET_ALL}")

# Starting message
print(Fore.MAGENTA + " Starting Network Sniffer (capturing 20 packets)...\n" + Style.RESET_ALL)

# Start sniffing: capture 20 packets only, call process_packet for each, don't store them
sniff(prn=process_packet, store=False, count=20)

# Ending message
print(Fore.CYAN + f"\n Sniffing complete! {packet_count} packets captured." + Style.RESET_ALL)
