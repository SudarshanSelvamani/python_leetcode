def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter_word = 0
    s = ''
    for i in secretWord:
      if i in lettersGuessed:
        counter_word += 1
        s += i
        s += ' '
      else:
        s += '_'  
        s += ' '
    return (len(secretWord) == counter_word , s)    
print(isWordGuessed('apple',['p','e','k']))