def tribonacci(signature, n):
  res = signature[:n] #take n amount of items from signature to res, not exceed value of n, if signature has less than n take all that 
  print(res)
  for i in range(n - 3): res.append(sum(res[-3:])) #since res already has 3 elements u only have to add remainin of n elements so n-3
  print('now res is',res)
  return res
tribonacci([1,2,3], 10)  
