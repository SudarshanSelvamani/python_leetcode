def isIn(char, aStr):
    aStr.lower()
    if len(aStr) == 0:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    
    elif char != aStr[int(len(aStr)/2)] and len(aStr) == 1:
        return False       
    else:
        if char > aStr[int(len(aStr)/2)]:
            return isIn(char,aStr[int(len(aStr)/2):]) 
        else:
            return isIn(char,aStr[:int(len(aStr)/2)]) 
print(isIn('k','abcdefg'))
               

        

