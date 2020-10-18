from scapy.all import *

def print_query_name(dns_packet):
	print(dns_packet[DNSQR].qname)
	
def filter_dns(packet):
	return DNS in packet and packet[DNS].opcode == 0 and DNSQR in packet and packet[DNSQR].qtype == 1

print("Sniffing visited websites...")
sniff(count=1000, lfilter=filter_dns, prn=print_query_name)