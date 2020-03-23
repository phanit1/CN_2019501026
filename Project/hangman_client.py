import socket

def main() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 8189))
    print(s.recv(1024).decode())
    choice = input("Enter your choice: ")
    s.send(choice.encode())
    if (s.recv(1024).decode().find("Enter your user name:") != -1) :
        inputName = input("Enter your name : ")
        s.send(inputName.encode())
    welcomeMsg = s.recv(1024).decode()
    print(welcomeMsg)

    while True :
        inputLetter = input("Enter a letter: ")
        s.send(inputLetter.encode())
        receivedMsg = s.recv(1024).decode()
        print(receivedMsg)
        if (receivedMsg.find("Your score") != -1) :
            break
    s.close()

if __name__ == "__main__" :
    main()