import math


for i in range(7):
    n = 10 ** i
    approximation = n/2*math.sin(2*math.pi/n)
    print("n:", n)
    print("Approximation:", approximation)
    print("Relative Error:", abs((approximation - math.pi)/math.pi))