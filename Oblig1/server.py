#import socket module
from socket import *
import _thread as thread
from threading import activeCount


def handleClient(connectionSocket):    
    try:
        message = connectionSocket.recv(2048).decode()
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
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())

    finally:
        connectionSocket.close()
    
    

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Write your code here
PORT = 6789

try:
    serverSocket.bind(('', PORT))
except:
    print("Bind failed. Error: " )

serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    thread.start_new_thread(handleClient, (connectionSocket,)) 
serverSocket.close()

