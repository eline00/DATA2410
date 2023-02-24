"""
Server side: it simultaneously handle multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
from socket import *
import _thread as thread
from threading import activeCount
import time
import sys


#this is too keep all the newly joined connections! 
all_client_connections = []

def now():
	"""
	returns the time of day
	"""
	return time.ctime(time.time())

def handleClient(connection, addr):
	"""
	a client handler function 
	"""
	
	all_client_connections.append(connection)
 
	message = f"[NEW CONNECTION] {addr} connected."
	broadcast(connection, message)
	connection.send("Welcome!".encode())
	
	
	try:
		while True:
			message = connection.recv(2048).decode().strip()
			print (now() + " " +  str(addr) + "#  ", message)
   
			if message == "exit":
				print(f"{addr} has left the server.")
				broadcast(connection, f"{addr} has left the server.")
				break
			
			broadcast(connection, f"[{addr}] {message}")
			connection.send("Message recieved".encode())
	except:
		all_client_connections.remove(connection)
		

def broadcast(connection, message):
	print ("Broadcasting")
	
	for i in all_client_connections:
		if (i != connection):
			i.send(message.encode())
	

def main():
	"""
	creates a server socket, listens for new connections,
	and spawns a new thread whenever a new connection join
	"""
	serverPort = 12000
	serverSocket = socket(AF_INET,SOCK_STREAM)
	try:
		serverSocket.bind(('', serverPort))
	except: 
		print("Bind failed. Error : ")
		sys.exit()
	serverSocket.listen(1)
	print(f"[LISTENING] server is listening on {gethostbyname(gethostname())}")
	print ('The server is ready to receive')
	while True:
		connectionSocket, addr =   serverSocket.accept()
		 
		print('Server connected by ', addr) 
		print('at ', now())
		thread.start_new_thread(handleClient, (connectionSocket,addr)) 
	serverSocket.close()

if __name__ == '__main__':
	main()
	



