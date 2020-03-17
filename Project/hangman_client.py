import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
while True:
    inpt = input("Enter a letter:")
    clientsocket.send(bytes(inpt, 'UTF-8'))
