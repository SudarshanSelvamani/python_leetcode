def inappropriate(str1):
    return str1[:int((len(str1)-(len(str1)-2)-1))]+int(len(str1)-2)*'*'+str1[int(len(str1)-1):] # XD
print(inappropriate('the'))
