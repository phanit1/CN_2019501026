import random

def isWordGuessed(secretWord, lettersGuessed):
  for i  in secretWord:
    if i not in lettersGuessed:
      return False
  return True

def getGuessedWord(secretWord, lettersGuessed):
  r=""
  for i in secretWord:
    if i in lettersGuessed:
      r = r + i
    else:
      r = r + "_ "
  return r

def getAvailableLetters(lettersGuessed):

  new = ""
  strr="abcdefghijklkmnopqrstuvwxyz"
  for i in strr:
    if i not in lettersGuessed:
      new = new + i
  return new

def hangman(s):
  print("Welcome to the game, Hangman!")
  print(f"I am thinking of a word that is {len(secretWord)} letters long")
  print("-"*10)
  guesses = 6
  lettersGuessed = []
  neww=[]
  while guesses > 0:
    print(f"You have {guesses} guesses left")
    print("Available letters:", getAvailableLetters(lettersGuessed))
    lg=input("Enter letter:")
    lg=lg.lower()
    sc="~!@#$%^&*()_+=~{}[]:;\"\'<,>.?/|\'1234567890\\"
    if lg not in sc:
        if lg in secretWord and lg not in lettersGuessed:
          neww.append(lg)
          print("Good Guess:", getGuessedWord(secretWord, neww)) 
          print("-"*10)
        elif lg not in secretWord and lg not in lettersGuessed:
          guesses -= 1
          print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
          print("-"*10)
        elif lg in lettersGuessed:  
          print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
          print("-"*10)
        if isWordGuessed(secretWord, neww): 
          print("Congratulations, you won!")
          break
        lettersGuessed.append(lg)
    else:
      print("Enter a valid input")
    if guesses == 0:
        print("Sorry, you ran out of guesses")
        print("SecretWord is " + secretWord)
f = open("words.txt").read().split()
secretWord=random.choice(f)
hangman(secretWord)