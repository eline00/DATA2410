from socket import *
import sys 

# creating a clinet socket
clientSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print("Usage: client.py <server_host> <server_port> <filename>")
    sys.exit(1)
    
HOST = sys.argv[1]
PORT = int(sys.argv[2])
filename = sys.argv[3]

# connecting to the server
clientSocket.connect((HOST, PORT))

# sending HTTP GET request to server
message = "GET /" + filename + "HTTP/1.1\r\nHost: " + HOST + "\r\n\r\n"
clientSocket.send(message.encode())

# response from server
response = clientSocket.recv(1024)

# printing response
print(response.decode())

clientSocket.close()
sys.exit()