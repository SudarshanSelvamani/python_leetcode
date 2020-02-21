def mean_error(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append((list1[i]-list2[i])**2)
    print('the answer is ', sum(list3)/len(list3))

    return sum(list3)/len(list3)
mean_error([-1, 0],[0, -1]) 