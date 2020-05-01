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
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))           