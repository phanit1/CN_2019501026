import socket, random
import sys
import threading

def isWordGuessed(secretWord,letterGuessed) :
    c = 0
    for i in secretWord:
        if i in letterGuessed:
            c += 1
    if c == len(secretWord):
        return True
    return False

def getGuessedWord(secretWord,lettersGuessed) :
    l1 = []
    for i in range(len(secretWord)):
        l1.append("_")
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            l1[i] = secretWord[i]
    return " ".join(l1)

def getAvailableLetters(lettersGuessed) :
    x = "abcdefghijklmnopqrstuvwxyz"
    y = list(x)
    for i in lettersGuessed:
        y.remove(i)
    return " ".join(y)

def hangman(secretWord, player_name, connection) :
    l = len(secretWord)
    guesses = 8
    wrongGuess_count = 0
    lettersGuessed = []
    welcomeMsg = "Welcome to the game, Hangman!" + str(player_name.user) + "\nI am thinking of a word that is " + str(l) + " letters long" + "\nYou have guesses " + str(guesses) + " left"
    connection.send(welcomeMsg.encode())
    
    while guesses != 0 :
        user_guess = connection.recv(1024).decode()
        if user_guess in lettersGuessed :
            avail_letters = getAvailableLetters(lettersGuessed)
            alreadyGuessed = "Already guessed " + str(user_guess) + ".\nTry another letter" + ".\nYou have " + str(guesses) + " remaining." + "\nAvailable letters: " + avail_letters
            connection.send(alreadyGuessed.encode())
            continue

        if user_guess in secretWord :
            lettersGuessed.append(user_guess)
            word = getGuessedWord(secretWord, lettersGuessed)
            avail_letters = getAvailableLetters(lettersGuessed)
            correctGuess = "Correct guess\n" + word + " is guessed till now. " + "\nYou have " + str(guesses) + " remaining. " + "\nAvailable letters: " + avail_letters
            isFound = isWordGuessed(secretWord, lettersGuessed)
            if isFound == True :
                N = len(secretWord)
                M = wrongGuess_count
                score = (10 - M) * N
                player_name.score += score

                sorted_users = sorted(users)
                lb = list()
                for i in sorted_users :
                    lb.append(i.leaderBoard())
                ld = "\n".join(lb)
                gc = "You guessed the word correctly: " + str(secretWord) + "\nYou have remaining guesses: " + str(guesses) + "\nYour score: " + str(score) + "\n" + ld
                connection.send(gc.encode())
                connection.close()
                break
            connection.send(correctGuess.encode())
            continue

        else :
            wrongGuess_count += 1
            lettersGuessed.append(user_guess)
            word = getGuessedWord(secretWord, lettersGuessed)
            avail_letters = getAvailableLetters(lettersGuessed)
            guesses -= 1
            wrongGuess = "Wrong guess. " + word + "\nYou have remaining guesses: " + str(guesses) + "\nAvailable letters: " + avail_letters
            connection.send(wrongGuess.encode())
            continue
    
    if guesses == 0 :
        score = 0
        player_name.score += score
        lostGame = "You lost the game. Try again!" + "\nThe secret word is: " + str(secretWord) + "\nYour score: " + str(score) + "\n"
        connection.send(lostGame.encode())
        connection.close()

class Hangman_Users :

    words = list()
    def __init__(self, user, score, word):
        self.user = user
        self.score = score
        self.words.append(word)

    def leaderBoard(self) :
        return '{},{}'.format(str(self.user).ljust(15), str(self.score))

def th(s) :
    conn, address = s.accept()
    user_existing = conn.send("New user? or Existing user?".encode())
    user_choice = conn.recv(1024).decode()
    if (user_choice == "new") :
        conn.send("Enter your user name: ".encode())
        user_name = conn.recv(1024).decode()
        user_names.append(user_name)
        f = open("words.txt").read().split()
        secretWord = random.choice(f)
        print(secretWord)
        user = Hangman_Users(user_name, 0, secretWord)
        users.append(user)
        hangman(secretWord, user, conn)
    else:
        conn.send("Enter your user name: ".encode())
        user_name = conn.recv(1024).decode()
        u_name = None
        for un in users :
            if (user_name in un.user) :
                u_name = un
                break
        f = open("words.txt").read().split()
        secretWord = random.choice(f)
        print(secretWord)
        user = Hangman_Users(user_name, 0, secretWord)
        hangman(secretWord, user, conn)

def main() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 8089))
    s.listen()
    n = 1000
    th_user = list()
    for i in range(n) :
        t1 = threading.Thread(target = th, args = (s,))
        th_user.append(t1)
        th_user[i].start()

    for i in range(n) :
        th_user[i].join()

    print("Done")

users = list()
user_names = list()
if __name__ == "__main__" :
    main()