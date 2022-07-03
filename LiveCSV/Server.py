import socket
import pickle
import csv

hostname = socket.gethostname()
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((hostname,port))
s.listen(1)

client, address = s.accept()
print(f'{address} is host ip address')
while True:
    client.send(bytes("WELCOME","UTF-8"))

    data = client.recv(4096)
    data = pickle.loads(data)
    print(data)

    csv_file = "Names.csv"
    try:
        with open('receiver.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            for i in data:
                writer.writerow(i)
    except IOError:
        print("I/O error")