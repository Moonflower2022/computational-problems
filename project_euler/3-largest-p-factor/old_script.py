import math
x = 600851475143
factorList = []


for i in range(int(math.sqrt(x))):
  if x%(i+1) == 0:
    factorList.append(i+1)
    x = x/(i+1)
    
print(max(factorList))
