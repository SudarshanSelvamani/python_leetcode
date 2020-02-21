count_list = []
def counting_bits(n):
    if n > 1:
        counting_bits(n // 2)
    i = n % 2 
    count_list.append(i)
    print(count_list)
    return count_list
def forfunction(listofsomething):
    p = 0    
    for i in range(len(listofsomething)):
        if  listofsomething[i] == 1:
            p += 1
    print(p)
    return p

counting_bits(5)
forfunction(count_list)        