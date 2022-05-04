import time 
from tempfile import NamedTemporaryFile
import csv 
import shutil
import pickle
import socket 

hostname = socket.gethostname()
port = 1234

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((hostname,port))

fields = []
test_csv = 'Stored.csv'
temp_file = NamedTemporaryFile(mode='w', delete=False)

while True:

    with open('Stored.csv', 'r') as csv_file, NamedTemporaryFile(mode='w', delete=False) as temp_file:
        reader = csv.DictReader(csv_file, fieldnames=fields)

        for row in reader:
            print(row)

            lis = row.values()
            reader_lists = list(lis)
            print(reader_lists)

            pic = pickle.dumps(reader_lists)
            print(pic)

            # s.send(pic)
            time.sleep(2)
    shutil.move(temp_file.name, test_csv)