from scapy.all import *
import time
import sys

def format_print(word1, word2, word3):
	print("{:<10} {:<10} {}".format(word1, word2, word3))

if len(sys.argv) < 2:
	print("Please provide destination IP.")
	quit()

DEST = sys.argv[1]
MAX_HOPS = 30


print(f"Tracing route to {DEST} over a maximum of {MAX_HOPS} hops: ")

format_print("n", "DTime", "IP")

t0 = time.time()
t2 = time.time()
i = 1
while i <= MAX_HOPS:
	packet = IP(dst=DEST, ttl=i) / ICMP()
	t1 = time.time()
	response = sr1(packet, timeout=2, verbose=0)
	t2 = time.time()
	if not response:
		format_print(i, round(t2-t1, 3), "Request timed out")
		i += 1
		continue
	format_print(i, round(t2-t1, 4), response[IP].src)
	i += 1
	if response[IP].src == Net(DEST):
		break 
		
print()
print(f"Finished in {t2-t0} seconds")  