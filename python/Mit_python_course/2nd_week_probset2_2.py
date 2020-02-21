def multipleof10(balance , annualintrestrate):
    monthlyintrestrate = annualintrestrate/12
    balance =balance + (balance*annualintrestrate)
    pay = 10
    b = 0
    while balance - (pay*13)>= 0:
        b = balance - (pay*13)
        print('the', balance)
        print(pay)
        pay += 1
       # print(pay)
multipleof10(3329, 0.2)         