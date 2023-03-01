#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Write your code here
HOST = ''
PORT = 6789

serverSocket.bind(HOST, PORT)
serverSocket.listen(1)

#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	
	try:
		request = connectionSocket.recv(1024).decode()
  
		message = request
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read
		f.close()

		#Send one HTTP header line into socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
		connectionSocket.send("HTTP/1.1 404 File Not Found\r\n\r\n".encode())

		
		#Close client socket
		connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
