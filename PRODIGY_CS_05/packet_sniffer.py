from scapy.all import sniff,raw
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Determine protocol type
        if protocol == 6:
            proto_name = 'TCP'
        elif protocol == 17:
            proto_name = 'UDP'
        else:
            proto_name = 'Other'

        # Display packet information
        print(f'Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto_name}')

        # If the packet has a TCP or UDP layer, display port information
        if TCP in packet or UDP in packet:
            layer = packet[TCP] if TCP in packet else packet[UDP]
            src_port = layer.sport
            dst_port = layer.dport
            print(f'Source Port: {src_port}, Destination Port: {dst_port}')

        # Display payload data
        if raw in packet:
            payload = packet[raw].load
            print(f'Payload: {payload}')
        print('-' * 50)

def start_sniffing(interface):
    print(f'Starting packet sniffing on interface {interface}...')
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Packet sniffer tool for educational purposes.')
    parser.add_argument('interface', help='The network interface to sniff on (e.g., eth0, wlan0)')
    args = parser.parse_args()

    start_sniffing(args.interface)
