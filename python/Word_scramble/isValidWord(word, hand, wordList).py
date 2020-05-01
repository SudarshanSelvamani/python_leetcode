def isValidWord(word, hand, wordList):
   
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings

    """
    lop = 0
    dp = hand.copy()
    if word in wordList:
        try:
            for letter in word:
                if dp[letter] != 0:
                    lop = dp[letter] 
                    dp[letter] = dp[letter]-1
                else:
                    return False    

            return True    
        except KeyError:
            return False  
    else:
        return False        
wordList = 'hello'            
print(isValidWord('hello', {'h': 1, 'e': 1, 'l': 1, 'o': 1},wordList))              
