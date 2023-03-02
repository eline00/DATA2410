from socket import *
import sys 

# creating a clinet socket
clientSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
	print("Usage: webclient.py <server_host> <server_port> <filename>")
	sys.exit(1)
	
HOST = sys.argv[1]
PORT = int(sys.argv[2])
filename = sys.argv[3]


# connecting to the server
clientSocket.connect((HOST, PORT))

# sending HTTP GET request to server
request = "GET /" + filename + " HTTP/1.1\r\nHost: " + HOST + "\r\n\r\n"
clientSocket.send(request.encode())

message = b''
while True:
	data = clientSocket.recv(2048)
	if not data:
		break
	message += data
	
# response from server
# response = clientSocket.recv(2048)

# printing response
print(message.decode())

clientSocket.close()
sys.exit()