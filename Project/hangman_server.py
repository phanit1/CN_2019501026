import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
   connection, address = serversocket.accept()
   buf = connection.recv(64)
   print(str(buf, "utf-8"))
   word = str(buf, "utf-8")
   break

print(word)

HANGMANPICS = ['''
+-----+
|     |
|
|
|
|
======= ''','''
+-----+
|     |
|     0
|
|
|
======= ''','''
+-----+
|     |
|     0
|     |
|
|
======= ''','''
+-----+
|     |
|     0
|    /|
|
|
======= ''','''
+-----+
|     |
|     0
|    /|\ 
|
|
======= ''','''
+-----+
|     |
|     0
|    /|\ 
|    / 
|
======= ''','''
+-----+
|     |
|     0
|    /|\ 
|    / \ 
|
======= ''' ]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	print(HANGMANPICS[len(missedLetters)])
	print()
	
	print('Missed letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)): # replace blanks with correctly guessed letters
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
	
	for letter in blanks: # show the secret word with spaces in between each letter
		print(letter, end=' ')
	print()
	
def getGuess(alreadyGuessed):
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess
			
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = word
gameIsDone = False

while True:
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		foundAllLetters = True
		
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is "' + secretWord + '"! You have won!')
			clientsocket.send(bytes('You lost opponent won', 'UTF-8'))
			gameIsDone = True
			break
	else:
		missedLetters = missedLetters + guess
		if len(missedLetters) == len(HANGMANPICS) - 1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
			gameIsDone = True
			break