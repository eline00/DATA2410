from socket import *

def main():
    PORT = 12000
    SERVER = '127.0.0.1'

    server = socket(AF_INET, SOCK_STREAM)

    server.bind((SERVER, PORT))
    server.listen(1)
    print('Server is ready to recieve')

    while True:
        conn, addr = server.accept()
        message = conn.recv(2048).decode()
        conn.send(message.encode())
        conn.close()
        server.close()
        
if __name__ == '__main__':
    main()
    
