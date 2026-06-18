from scapy.all import rdpcap, IP

file = input("Enter PCAP file name: ")

packets = rdpcap(file)

print("\nNETWORK PACKET ANALYZER")
print("=" * 50)

for i, packet in enumerate(packets, start=1):

    if packet.haslayer(IP):
        print(f"\nPacket {i}")
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)
        print("-" * 50)

print("\nAnalysis Completed")