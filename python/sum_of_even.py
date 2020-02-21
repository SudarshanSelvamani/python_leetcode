mylist = []
n = int(input())
for i in range(n):
    ele = int(input())
    mylist.append(ele)
def sum_of_even(list_given):
    p = 0
    for i in list_given:
        if i % 2 == 0:
            p += i
    print(p)
sum_of_even(mylist)            