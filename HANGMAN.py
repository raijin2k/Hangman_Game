#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
HANGMAN = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
words = 'abhirup atanu chaitanya kishan karthikeya viswadruth'.split()

def randword(wordList):
     # returns a random string from the passed list of strings.
     index = random.randint(0, len(wordList) - 1)
     return wordList[index]

def display(ml, cl, hidden):
     print(HANGMAN[len(ml)])
     print()
     print('Missed letters are', end=' ')
     for l in ml:
         print(l, end=' ')
     print()

     blank = '_' * len(hidden)

     for i in range(len(hidden)): # replace blanks with correctly guessed letters.
         if hidden[i] in cl:
             blank = blank[:i] + hidden[i] + blank[i+1:]

     for l in blank: # Show the secret word with spaces in between each letter.
         print(l, end=' ')
     print()

def Guess(guessed):
     # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
     while True:
         print('Guess a letter')
         guess = input()
         guess = guess.lower()
         if len(guess) != 1:
             print('Please enter a single letter.')
         elif guess in guessed:
             print('You have already guessed that letter. Try again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Not a letter!')
         else:
             return guess

def playAgain():
     # This function returns True if the player wants to play again; otherwise, it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')


print('WELCOME TO HANGMAN')
ml = ''
cl = ''
hidden = randword(words)
gameOver = False

while True:
     display(ml, cl, hidden)

     # Let the player enter a letter.
     guess = Guess(ml + cl)

     if guess in hidden:
         cl += guess

         # Check if the player has won.
         foundAll = True
         for l in range(len(hidden)):
             if hidden[l] not in cl:
                 foundAll = False
                 break
         if foundAll:
             print('The hidden word was "' + hidden +
                   '"! Congratulations you have won!')
             gameOver = True
     else:
         ml += guess

         # Check if player has guessed too many times and lost.
         if len(ml) == len(HANGMAN) - 1:
             display(ml, cl, hidden)
             print('You have run out of guesses!\nAfter ' + str(len(ml)) + ' missed guesses and ' + str(len(cl)) + ' correct guesses, the word was "' + hidden + '"')
             gameOver = True

     # Ask the player if they want to play again (but only if the game is done).
     if gameOver:
         if playAgain():
             ml = ''
             cl = ''
             gameOver = False
             hidden = randword(words)
         else:
             break


# In[ ]:





# In[ ]:




