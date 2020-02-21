ROMAN_MAP = (
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
        ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
        ('IV', 4), ('I', 1)
)

def solution(roman):
    """Transform the roman numeral into an integer.
    Keyword arguments:
    roman -- Roman numeral as a string of allowed characters
    Return corresponding numeric decimal integer.
    """
    result = 0
    index = 0
    for rom, arab in ROMAN_MAP:
        print('in the for loop',rom ,'and',arab)
        print('index:',index, 'length of rom is:',len(rom))
        while roman[index : index+len(rom)] == rom:
            print('this is what roman index is: ',roman[index : index+len(rom)])
            print('this is what rom is: ',rom)
            print('arab is',arab)
            result += arab
            index += len(rom)
            print('length of rom =',len(rom))
            print('this is what index is ',index)
    print(result)
solution('MCMXC')    