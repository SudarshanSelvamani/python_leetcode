def oddTuples(aTup):
    tup = ()
    for i in range(0, len(aTup), 2):
        tup += (aTup[i],)
        
    return tup
#print(oddTuples(('this','is','a','test','tuple','!','lop')))           
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))           

