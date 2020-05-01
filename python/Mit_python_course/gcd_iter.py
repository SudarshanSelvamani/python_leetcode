def gcdIter(a, b):
    gcd = 1
    mylist = []
    c = min(a, b)
    while c > 1:
        if a % c == 0 and b % c == 0:
            gcd = c
            mylist.append(gcd)

        c -= 1
    return max(mylist)
print(gcdIter(20 , 180))