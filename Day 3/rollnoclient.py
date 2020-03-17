import socket

host = 'localhost'
port = 8188

soc = socket.socket()
soc.connect((host, port))
print('\n-------MSIT Attendance marking - 2019-------\n')
print('Enter your rollnumber : ')
rollnum = input()
soc.send(rollnum.encode())
soc.close()