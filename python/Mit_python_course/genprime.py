def genPrimes():
    v = 1
    result = []
    while True:
        v += 1
        for x in result:
            if v % x == 0:
                break     
        else:
            result.append(v)
            yield v
lolly = genPrimes()
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())
print(lolly.__next__())

