import socket
import threading
import os
import time
import sys

def receiver():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((ip_sender,port_sender))
	while True:
		msg=s.recvfrom(1024)
		print("\n"+msg[0].decode())
		if "exit" in msg[0].decode() or "bye" in msg[0].decode():
			sys.exit()
def sender():
	c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	text="hello"
	while True:
		if "bye" in text or "exit" in text or "finish" in text:
			exit()
		else:		
			text=input(f'{name}:')
			text= name+":"+text
			c.sendto(text.encode(),(ip_receiver,port_receiver))


print("				-------------------------Configuration------------------------      ")
ip_receiver=input("\nEnter the IP of Reciever:")
port_receiver=int(input("\nEnter the Port of the Reciever:"))
ip_sender=input("\nEnter the your IP :")
port_sender=int(input("\nEnter the your Port:"))
name=input("Enter your System's name:")


print("-----------------------Connecting-----------------------")
time.sleep(1)
print("-----------------------Connected-------------------------")


send=threading.Thread(target=sender)
recieve=threading.Thread(target=receiver)
send.start()
recieve.start()