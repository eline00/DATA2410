#import socket module
from socket import *
import _thread as thread
import threading

"""
 This function takes a client connection and an addr tuple, containing the IP address and port number, as arguments. Then, it attempts
 to recieve an HTTP request from the client which it parses to extract the filename. The file is then opened read so that its content
 can be sent back to the client, with an HTTP 200 OK header. If the file is not found an HTTP 404 Not FOund message is sent instead.
"""
def handleClient(connectionSocket, addr):   
    # broadcasting that a new client has connected 
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        # recieving message from client 
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1][1:]		# extracts the filename from the GET message sent from the client
        
        # opening and reading the file, and saving its content in outputdata
        with open(filename, "rb") as f:
            outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('\r\n'.encode())		# linebreak

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i+1]) 

    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('\r\n'.encode())		# line break
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())

    finally:
        # closing the connection
        connectionSocket.close()
    
    
# creating a server socket
serverSocket = socket(AF_INET, SOCK_STREAM) 

# creating a server port
PORT = 6789

# attempting to bind the socket to the host and port
try:
    serverSocket.bind(('', PORT))
except:
    print("Bind failed. Error: " )

serverSocket.listen(1)

# printing that the server is listening and ready to serve
print(f"[LISTENING] server is listening on {gethostbyname(gethostname())}")
print('Ready to serve...')

while True:
    # accepts incoming client connections
    connectionSocket, addr = serverSocket.accept()
    
    # starting a thread to serve multiple requests simultaneously
    thread.start_new_thread(handleClient, (connectionSocket, addr)) 
serverSocket.close()

