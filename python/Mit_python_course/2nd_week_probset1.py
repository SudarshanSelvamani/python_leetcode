#def remaining_balance(balance = 42, annualIntrestrate = 0.2 , monthlypaymentrate = 0.04 ):
   # unpaid = balance - (monthlypaymentrate*balance)
    #balance = unpaid
   # for i in range(12):
    #    monthly_intrest_rate = annualIntrestrate/12
     #   minimum_monthly_pay = monthlypaymentrate*balance
      #  unpaid = balance - minimum_monthly_pay
       # balance = unpaid + (monthly_intrest_rate*unpaid)



        
        
    #print('the ',i+1,'month balance is', balance)    

#remaining_balance(484, 0.2, 0.04)"""


def finish_amount(balance, annualIntrestrate, monthlypaymentrate)
    n = 0
    while balance > 0:
        monthly_intrest_rate = annualIntrestrate/12
        minimum_monthly_pay = monthlypaymentrate*balance
        unpaid = balance - minimum_monthly_pay
        balance = unpaid + (monthly_intrest_rate*unpaid)
        n += 1
    print(n)
finish_amount(482, 0.2, 0.04)        


    
