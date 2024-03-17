va = 0
for i in range(1000):
  va = va + (i+1)**(i+1)
print(va % 10000)
