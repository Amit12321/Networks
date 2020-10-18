from scapy.all import *

def filter_length(packet): 
	return UDP in packet and packet[UDP].dport == 8820

def filter_msg(packet):
	return UDP in packet and Raw in packet and packet[Raw].load == b''

len_packet = sniff(count=1, lfilter=filter_length)
len_msg = int(len_packet[0][Raw].load)

msg = ""

packets = sniff(count=len_msg, lfilter=filter_msg)
for i in range(len_msg):
	msg += chr(packets[i][UDP].dport)


print("Recieved Message: ", msg)
print("Quitting...")

