import re
def pig_it(pigs):
    pig = []
    pi = re.split(' ',pigs)
    print(pi)
    for i in range(len(pi)):
        if pi[i].isalpha():
            p = pi[i]
            p = p[1:]+p[:1]
            p += 'ay'
            pig.append(p)
        else:
            p = pi[i]
            pig.append(p)    
    
    #print(p)
    #print(pig)
    print(' '.join(pig))
    #return pi



pig_it('Start small, but will succeed!!')    