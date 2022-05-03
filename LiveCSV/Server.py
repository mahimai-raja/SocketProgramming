import pickle
import socket
import pyfiglet

hostname = socket.gethostname()
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((hostname,port))
s.listen(1)

conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    conn.send(bytes("WELCOME","UTF-8"))

    data = conn.recv(4096)
    data = pickle.loads(data)
    data = data
    print(data)
