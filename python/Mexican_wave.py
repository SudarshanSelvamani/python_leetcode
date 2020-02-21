def mexican_wave(s):
    up = s
    li1 = []
    for i in range(len(s)):
        if up[i] != ' ':
            if i == 0:
                str1 = up[i].upper()
                up = list(up)
                up[i] = str1
                up = ''.join(up)
                li1.append(up)    
            else:
                str1 = up[i].upper()
                str2 = up[:i].lower()
                up = list(up)
                up[i] = str1
                up[:i] = str2
                up = ''.join(up)
                li1.append(up)

       
    return li1, len(li1)    
print(mexican_wave('two words'))        
        
