def pete_innapropriate(str1,list1=[]):
    list4 = str1.split()
    
    for word in list1:
        word = word.lower()
    for i in range(len(list4)):
        if list4[i-1].isalpha() or (list4[i-1][-1]) != '.':
            list4[i] = list4[i].lower()
    
        if (list4[i].isupper() and len(list4[i]) > 2) or (list4[i][0].isupper()):
            
            list4[i] = list4[i].lower()
            list4[i] = list4[i].capitalize()
        else:
            list4[i] = list4[i].lower()
            
    print(list4)        


    for i in range(len(list4)):
        if len(list4[i]) > 2:
            if list4[i] not in list1:
                if list4[i].isalpha():
                    list4[i] = ((list4[i])[0])+(len(list4[i])-2)*'*'+((list4[i])[-1])

                else:
                    list4[i] = ((list4[i])[0])+(len(list4[i])-3)*'*'+((list4[i])[-2:])
                    
                
            
                
                           
    list4[i] = list4[i].capitalize()            
    print(list4)
    str1 = ' '.join(list4)
    print(str1)
pete_innapropriate("Uh!")