# Hangman game
#

# ----------------------------------

import random

WORDLIST_FILENAME = "words.txt" #the path of the file

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter_word = 0
    for i in secretWord:
      if i in lettersGuessed:
        counter_word += 1
    return len(secretWord) == counter_word    




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for i in secretWord:
        if i in lettersGuessed:
        
            s += i
        else:
            s += '_'  
    return s




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l = ' '
    lettersGuessed.sort()
    for i in alphalist:
        if i not in lettersGuessed:
            l += i
    return l
    

def hangman(secretWord):
    asciihanglsit = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print('Welcome to the game hangman!')
    print('I am thinking of a word that is ', len(secretWord),'letters long')
    lettersGuessed= []
    guess = 6
    j = 0
    done = True
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    while guess >= 0 and done:
        print('-----------')
        print(asciihanglsit[j])
        
       
        if isWordGuessed(secretWord,lettersGuessed):
            print('Congratulations, you won!')
            break
        elif guess == 0:
            #print(asciihanglsit[abs(guess - 7)])
            print('Sorry, you ran out of guesses. The word was ',secretWord) 
            done = False
            break
        else:
            print('You have',guess,'guesses left')
            #print(getGuessedWord(secretWord, lettersGuessed))
            print('Available letters:',getAvailableLetters(lettersGuessed))
            g = str(input('Please guess a letter: '))
            if g not in lettersGuessed:
                lettersGuessed.append(g)
                if g not in secretWord:
                    print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
                    guess -= 1
                    j += 1
                   # print(asciihanglsit[abs(guess - 7)])

                else:
                    print('Good guess:',getGuessedWord(secretWord,lettersGuessed))
                    #print(asciihanglsit[abs(guess - 7)])

            else:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                #print(asciihanglsit[abs(guess - 7)])

    c = str(input('press c to close the program and r to refresh'))
    if c == 'c':
        return
    elif c == 'r':
        hangman(chooseWord(wordlist))           
 
            
hangman(chooseWord(wordlist))                








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
