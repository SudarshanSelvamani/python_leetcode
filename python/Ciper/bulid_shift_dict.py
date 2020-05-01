def build_shift(shift):
    first_dict = {'a': 1 ,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A': 61 ,'B':62,'C':63,'D':64,'E':65,'F':66,'G':67,'H':68,'I':69,'J':70,'K':71,'L':72,'M':73,'N':74,'O':75,'P':76,'Q':77,'R':78,'S':79,'T':80,'U':81,'V':82,'W':83,'X':84,'Y':85,'Z':86}
    second_dict = {}
    key_list = list(first_dict.keys())
    value_list = list(first_dict.values())
    
    for letter in first_dict.keys():
        val = first_dict[letter]
        val += shift
        if val > 26 and val < 60:
            val -= 26
        if val > 86:
            val -= 26
        pop = value_list.index(val)
        pop = key_list[pop]
        second_dict[letter] = pop

    return second_dict
print(build_shift(16))
def apply_shift(shift):
    '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
    '''
    message_text ='ABcD'
    shifted =''
    dict_shift = build_shift(shift)
    print(dict_shift)
    for letter in message_text:
        if letter.isalpha():
            if letter.isupper():
                var = letter.lower()
                var = dict_shift[var]
                var = var.upper()
                shifted += var
            else:
                var = dict_shift[letter]
                shifted += var    
        else:
            shifted += letter        
        
    return shifted
#print(apply_shift(3))
