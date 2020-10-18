from scapy.all import *

SERVER_IP = "192.168.1.50"
PORT = 8820 #This port will be initially used to send msg length.

print("Enter message to send: ")
msg = input()
length = len(msg)
packet = IP(dst=SERVER_IP) / UDP(sport=6666, dport=PORT) / str(length)
send(packet)

for l in msg:
	port = ord(l)
	packet = IP(dst=SERVER_IP) / UDP(sport=5555, dport=port) / ''
	send(packet)