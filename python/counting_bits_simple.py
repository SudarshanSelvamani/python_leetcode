count_list = []
def countBits(n):
    p = 0
    if n > 1:
        countBits(n // 2)
    i = n % 2 
    count_list.append(i)
    for i in range(len(count_list)):
        if count_list[i] == 1:
            p += 1
    print(p)        
    return p 
countBits(4)