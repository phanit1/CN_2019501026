import socket

soc = socket.socket()
soc.connect(('localhost', 8188))
print('\n-------MSIT Attendance marking - 2019-------\n')
# while True:
print('Enter your rollnumber : ', end = " ")
rollnum = input()
soc.send(rollnum.encode())
while True:
    data = soc.recv(1024).decode()
    if not data:
        continue
    print (str(data))
message = ''
while message != '.':
    soc.send(message.encode())
soc.close()