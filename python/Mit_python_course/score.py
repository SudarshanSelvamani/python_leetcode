def score(word, f):
    placeinalpha = 0
    list1 = []
    alpha = {'a': 1 ,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    word =  word.lower()
    if word == '':
        return 0
    for i in range(len(word)):
        placeinalpha = alpha[word[i]]*i
        list1.append(placeinalpha)
    #print(list1)   
    list1.sort(reverse=True) 
    score = f(list1[0],list1[1])
    fist_highest =max(list1)     
    #print(fist_highest)
    list1 = list(filter(lambda a: a != fist_highest,list1))
    se_highest = max(list1)
    #print(se_highest)
    score1 = f(fist_highest,se_highest)
    
    return (score1,score)
   # print(score)


    #print(list1)
def f(a,b):
    return a+b    
print(score('a',f))    
