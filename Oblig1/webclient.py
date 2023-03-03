from socket import *
import sys 

# creating a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)


if len(sys.argv) > 4:
	print("Wring input! It should be: webclient.py HOST PORT filename")
	sys.exit(1)

# takes the input arguments from the terminal  and defines argument 1 as host, 
# argument 2 as port, and argument 3 as filename
HOST = sys.argv[1]		
PORT = int(sys.argv[2])
filename = sys.argv[3]

# connecting to the server
clientSocket.connect((HOST, PORT))

# sending HTTP GET request to server
request = "GET /" + filename + " HTTP/1.1\r\nHost: " + HOST + "\r\n\r\n"
clientSocket.send(request.encode())

# response from server
message = b''		# empty byte object
while True:
	data = clientSocket.recv(2048)		# the data recieved from the server
	if not data:		# if no data is recieved the loop breaks
		break
	message += data		# appending the recieved data to message


# printing response
print(message.decode())

# closing the socket and exiting 
clientSocket.close()
sys.exit()

"""
RUN EXAMPEL:
Terminal > python Oblig1/webclient.py 127.0.0.1 6789 Oblig1/index.html
HTTP/1.1 200 OK

<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Oblig1</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>This is my oblig1 html</p>
</body>


With a filename that does not exist in the directory:
Terminal > python Oblig1/webclient.py 127.0.0.1 6789 Oblig1/index2.html
HTTP/1.1 404 Not Found

<html><body><h1>404 Not Found</h1></body></html>

"""