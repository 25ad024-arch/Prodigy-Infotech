from scapy.all import *

p1 = IP(src="192.168.1.10", dst="8.8.8.8")/TCP()/Raw(load="Hello")
p2 = IP(src="8.8.8.8", dst="192.168.1.10")/TCP()/Raw(load="Reply")
p3 = IP(src="192.168.1.10", dst="1.1.1.1")/UDP()/Raw(load="DNS Query")

wrpcap("data.pcap", [p1, p2, p3])

print("PCAP file created successfully!")