#Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# write server ip and port, and connect
clientPort = 12000
server = '127.0.0.1'
addr = (server, clientPort)



while True:

	""" we are going to use a select-based approach here because it will help
	us deal with two inputs (user's input (stdin) and server's messages from socket)
	"""
	inputs = [sys.stdin, client_socket]

	""" read the select documentations - You pass select three lists: the 
	first contains all sockets that you might want to try reading; the 
	second all the sockets you might want to try writing to, and the last 
	(normally left empty) those that you want to check for errors. """

	read_sockets, write_socket, error_socket = select.select(inputs,[],[])

	# we check if the message is either coming from your terminal or 
	# from a server
	for socks in read_sockets:
		if socks == client_socket:

			try:
				message = client_socket.recv(2048).decode()
				if not message: #when data doesn't get a connection to a server
					print("Connection to server lost. Exiting...") 
					break
				if "has left the chat" in message: #when a client has entered the "exit" msg 
					print(message)
					break
				print(message)
			except socket.error as e:
				print("No message from the server.", e)
				sys.exit()

		else:
			#takes inputs from the user
			message = sys.stdin.readline()

			#send a message to the server
			### write your code here ###
			client_socket.send(message.encode())
			### your code ends here ###

			
client_socket.close()
		