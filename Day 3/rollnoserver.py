import socket, os
print('\n-------MSIT Attendance marking - 2019-------\n')
roll_list = [2019501026, 2019501111, 2019501087, 2019501118, 2019501041, 2019501071, 2019501101]
string  = str(roll_list[0])
print('Students in the class: \n')
# for i in range(1, len(roll_list)):
# 	string = string + ' - ' +str(roll_list[i])
# print(string)
print(roll_list)
print("\n")

soc = socket.socket()
soc.bind(('127.0.0.1', 8188))
soc.listen(10)
while True:
	conn, addr = soc.accept()
	rollnum = conn.recv(1024).decode()
	checkroll = int(rollnum)
	if checkroll in roll_list:
		roll_list.remove(checkroll)
		print("Attendance Marked for " + rollnum+"\n")
		print("Absentees are "+ str(roll_list)+"\n")
	else:
		print("Roll Number is not found\n")
soc.close()