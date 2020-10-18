from scapy.all import *
import sys

def help():
	print("Please provide the IP Address you suspect.")
	sys.exit(1)

TIMEOUT = 5

def detect_promiscuous(ip):
	arp_packet = Ether(dst="ff:ff:ff:ff:ff:fe") / ARP(pdst=ip)
	response = srp1(arp_packet, timeout=TIMEOUT, verbose=0)
	if response:
		print(f"{ip} is in promiscuous mode.")
	else:
		print(f"{ip} is not in promiscuous mode.")

def main():
	if len(sys.argv) < 2:
		help()
	ip = sys.argv[1] # The ip address the user suspect.
	detect_promiscuous(ip)

main()
	

