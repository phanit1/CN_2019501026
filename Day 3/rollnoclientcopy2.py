import socket

soc = socket.socket()
print('\n-------MSIT Attendance marking - 2019-------\n')
# while True:
print('Enter your rollnumber : ', end = " ")
rollnum = input()
for i in range(8187,8190):
    soc.connect(('localhost', i))
    soc.send(rollnum.encode())
    soc.close()