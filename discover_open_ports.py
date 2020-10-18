from scapy.all import *
import sys

DST = sys.argv[1]

for i in range(20, 1030):
	syn = TCP(dport=i, seq=123, flags='S')
	syn_packet = IP(dst=DST) / syn
	res = sr1(syn_packet, timeout=2, verbose=0)
	if res:
		print(f"Port {res[TCP].sport}")
	
