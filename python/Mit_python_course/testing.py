#print(5//2)
#str12 = '123456'
#print(str12[0:2])
#"""num = 0
#lop = 0
#end = 6
#while num < end:
 #   num += 1
  #  lop += num
#print(lop)    
#string1 = 'Massachusetts Institute of Technology'
#print(len(string1))
#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0

#for char in school:
 #   if char == 'a' or char == 'e' or char == 'i' \
  #     or char == 'o' or char == 'u':
   #     numVowels += 1
    #elif char == 'o' or char == 'M':
     #   print(char)
    #else:
     #   numCons -= 1"""
#"""
#print('numVowels is: ' + str(numVowels))
#print('numCons is: ' + str(numCons)) 
#1
#"""
#"""
#def qua(a, b, c,):
 #   return a + 1
#a = 5
#print(qua(a,4,3))
#print(a)
#"""
#str1 = 'exterminate!'
#str2 = 'number one - the larch'
#print(str1.upper())
#list1 = [100, 0, 1, 4, 4, 1, 6, 3, 4]
#list2 = ['x', 'z', 't', 'q']
#print(list1+list2)
#def abs1(a):
#    for i in range(len(a)):
#        a[i] = abs(a[i])
#    return a        
#print(abs1([1, -4, 8, -9]))
def biggest(aDict):
   # best = max([len(value) for value in aDict.values()]
   best = max([ len(value) for value in aDict.values()])
   print('best is',best)
   #longest_value = 
   #print('dicr',aDict)
   return [key for key in aDict.keys() if len(aDict[key]) == best]


#ani = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': [3, 4]}))


#print(ani)   