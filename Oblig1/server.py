from socket import *
import sys

def main():
    PORT = 12000
    SERVER = '127.0.0.1'

    server = socket(AF_INET, SOCK_STREAM)

    try:
        server.bind((SERVER, PORT))
    except:
        print('Bind failed. Error: ')
        sys.exit()

    server.listen(1)

    while True:
        print('Server is ready to recieve')
        # Accept incoming connection
        conn, addr = server.accept()
        
        # Request data from the client
        request_data = conn.recv(2048).decode()
        print('Recieved request: ', request_data)
    
        # Parse the request to get the requested file name
        request_lines = request_data.split('\r\n')
        request_line = request_lines[0]
        request_parts = request_line.split()
        method = request_parts[0]
        path = request_parts[1]
        
        # If the request file does not exist it reterns a 404 response
        if not sys.path.exists("." + path):
            response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            conn.send(response.encode())
            conn.close()
            continue
        
        # Reading the file
        with open('.' + path, 'rb') as f:
            file = f.read()
            
        # Send response back to client
        response = 'HTTP/1.1 200 OK\r\n\r\n'
        conn.send(response.encode() + file)
        conn.close()
    server.close()
    sys.exit()
        
if __name__ == '__main__':
    main()
    
