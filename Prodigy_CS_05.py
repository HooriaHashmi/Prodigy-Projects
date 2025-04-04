from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

# Function to handle packet display and analysis
def packet_handler(packet):
    # Capture timestamp of when the packet was received
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Start building packet information string
    packet_info = f"Timestamp: {timestamp} - {packet.summary()}"
    
    # Check if packet contains IP layer
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        packet_info += f" | Source IP: {ip_src} -> Destination IP: {ip_dst}"
        
        # Check for transport layer protocols (TCP/UDP)
        if packet.haslayer(TCP):
            packet_info += f" | Protocol: TCP | Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            packet_info += f" | Protocol: UDP | Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}"
        else:
            packet_info += f" | Protocol: Other IP-based Protocol"

        # Display Payload if it exists (show first 50 bytes for safety)
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            packet_info += f" | Payload: {payload[:50]}"  # Show first 50 bytes of the payload

    # Print the packet information
    print(packet_info)

# Function to start sniffing network packets
def start_sniffing(packet_count=10, filter_condition=None):
    print("Starting packet capture...\n")
    
    # Sniff packets; if filter_condition is specified, apply it
    sniff(count=packet_count, prn=packet_handler, filter=filter_condition)

# Example Usage: Capture 10 packets on the network
start_sniffing(packet_count=10)
