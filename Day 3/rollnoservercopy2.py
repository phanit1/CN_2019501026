import socket, os
print('\n-------MSIT Attendance marking - 2019-------\n')
roll_list = [2019501026, 2019501111, 2019501087, 2019501118, 2019501041, 2019501071]
string  = str(roll_list[0])
print('Students in the class:')
for i in range(1, len(roll_list)):
	string = string + ' - ' +str(roll_list[i])
print(string)

soc = socket.socket()
soc.bind(('localhost', 8189))
soc.listen(10)
while True:
	conn, addr = soc.accept()
	print(str(addr) + ' connected:')
	rollnum = conn.recv(1024).decode()
	checkroll = int(rollnum)
	if checkroll in roll_list:
		roll_list.remove(checkroll)
		print(roll_list)
soc.close()