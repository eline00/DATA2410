#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Write your code here
HOST = '127.0.0.1'
PORT = 6789

serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
print('Ready to serve...')

#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	connectionSocket, addr = serverSocket.accept()
	
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1][1:]
		with open(filename, "rb") as f:
			outputdata = f.read()

		#Send one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
		connectionSocket.send('Content-Type: text/html\r\n'.encode())
		connectionSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
		connectionSocket.send('\r\n'.encode())

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])


	except IOError:
     	#Close client socket
  
		#Send response message for file not found
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
		connectionSocket.send('Content-Type: text/html\r\n'.encode())
		connectionSocket.send('\r\n'.encode())
		connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())

		connectionSocket.close()
		

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
