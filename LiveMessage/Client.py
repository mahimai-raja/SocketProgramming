import socket
import pyfiglet

hostname = socket.gethostname()    
port = 1234

# AF_INET refers IPv4 , SOCK_STREAM refers TCP 

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
Socket.connect((hostname,port))

# In TCP message is send in bytes so we need to decode to read 

msg = Socket.recv(1024)
msg = msg.decode('UTF-8')
msg = pyfiglet.figlet_format(msg)
print(msg)

while True :
    Input = input()
    Socket.send(bytes(Input,'UTF-8'))
    
    msg = Socket.recv(1024)
    msg = msg.decode('UTF-8')
    print(msg)


