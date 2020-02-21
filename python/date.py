import re
def american_date_to_europian_date():
    month={"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}

    date = str(input())
    d = re.split(', | |/|,',date)
    #print(d)
   # print(date)

    #date= date.split('/')
    if d[0].isalpha():
        mm = month[d[0]]
        #print('{0}/{1}/{2}'.format(d[1], mm, d[2]))
    else:
        mm = d[0]
    eudate = '{0}/{1}/{2}'.format(d[1], mm, d[2])     
    print(eudate)       

american_date_to_europian_date()    