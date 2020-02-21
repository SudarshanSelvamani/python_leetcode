var1 = 0
def finish_amount(balance, annualIntrestrate, monthlypayment):
    var1 += 0.02
    n = 0
    while balance >= 0.0001 and n <= 12 :
        monthly_intrest_rate = annualIntrestrate/12
        unpaid = balance - monthlypayment
        balance = unpaid + (monthly_intrest_rate*unpaid)
        print(balance)
        n += 1
    print(monthlypayment)
    print(n)
    print(balance)

    if balance > 0.0001:
        finish_amount(482, 0.2, var1) 
            
finish_amount(482, 0.2, 0.02)





    
