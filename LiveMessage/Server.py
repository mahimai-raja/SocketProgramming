import socket
import pyfiglet

hostname = socket.gethostname()
port = 1234

# AF_INET refers IPv4, SOCK_STREAM refers TCP 

Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
Socket.bind((hostname,port))
Socket.listen(6)           

while True:
    ClientSocket, address = Socket.accept()

    statusMsg = pyfiglet.figlet_format("CONNECTED")
    print(statusMsg)
    print(f"The host {address} is connected with the server")

# TCP uses bytes only to communicate , UTF-8 is common encryption

    ClientSocket.send(bytes("WELCOME !",'utf-8'))

    while True:
        ClientSocket.send(bytes("Send your message",'UTF-8'))

        msg = ClientSocket.recv(1024)
        msg = msg.decode('utf-8')
        print(msg)

        


