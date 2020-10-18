from scapy.all import *
from sys import argv 

domain = argv[1]
DNS_SERVER = "8.8.8.8"
dns_packet = IP(dst=DNS_SERVER) / UDP(sport=24600, dport=53) / DNS(qdcount=1) / DNSQR(qname=domain)
res = sr1(dns_packet)
print(res[DNSRR].rdata)