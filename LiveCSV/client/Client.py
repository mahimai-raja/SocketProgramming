import socket, pickle
import pyfiglet
import time

hostname = socket.gethostname()
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,port))


msg = s.recv(10)
msg = msg.decode('UTF-8')
print(pyfiglet.figlet_format(msg))


arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
data_string = pickle.dumps(arr)
print(data_string)



while True :
    s.send(data_string)
    time.sleep(3)