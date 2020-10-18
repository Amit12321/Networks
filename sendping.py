from scapy.all import *
from sys import argv

dst = sys.argv[1]
if len(argv) == 1:
	print("Please provide a destination IP address.")
	quit()
if len(argv) == 2:
	print("Missing number of packets. assuming it is 1...")
	num = 1
else:
	try:
		num = int(argv[2])
	except ValueError as e:
		print("Invalid Argument. Quitting...")
		quit()

print(f"Sending {num} packets to {dst}")
answers = 0

for i in range(num):
	ping = IP(dst=dst) / ICMP()
	if sr1(ping, verbose = 0, timeout=2):
		answers += 1
		print("Recieved answer")
	else:
		print("Request timed out.")

print(f"Received {answers} reply packets")
	
	