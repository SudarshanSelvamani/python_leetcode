def getSublists(L, n):
    m = 0
    lis1 = []
    lis2 = []
    while n <= len(L):
        #lis2 = L[m:n]
        lis1.append(L[m:n])
        m += 1
        n += 1
    return lis1    
print(getSublists([1, 1, 1, 1, 4],2))