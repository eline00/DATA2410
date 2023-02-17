from socket import *

def main():
    PORT = 12000
    SERVER = '127.0.0.1'

    client = socket(AF_INET, SOCK_STREAM)

    client.connect((SERVER, PORT))

    message = input('Write message here: ')
    client.send(message.encode())

    recieved_message = client.recv(2048).decode()
    print(recieved_message)

    client.close()
    
if __name__ == '__main__':
    main()