Packet Sniffer using Scapy

A simple network packet sniffer built with Python and Scapy. It captures 10 packets and displays their summary along with decoded payloads, if available.

Description

This script uses Scapy to listen to network traffic and print useful details about each packet:
- Source and destination IP addresses
- Protocol used
- Raw payload data (UTF-8 decoded)

It helps you understand how network data flows and the structure of basic packets.


 How to Run

 Step 1: Install Scapy

pip install scapy

Step 2: Run the script
sudo python packet_sniffer.py
