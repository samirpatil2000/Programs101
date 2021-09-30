import math
def maxPrimeFactors (n):
    temp=n
    maxPrime = -1
     
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2
         
    while n % 3 == 0:
        maxPrime = 3
        n=n/3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            maxPrime = i
            n = n / i
        while n % (i+2) == 0:
            maxPrime = i+2
            n = n / (i+2)
         
    if n > 4:maxPrime = n
    if math.sqrt(temp)<int(maxPrime):
        return "Strange"
    return "Not Strange"


# print(maxPrimeFactors(int(input())))



def fun2(x,y):
    if y==x*2:
        return "Yes"
    return "No"
x=int(input())
y=int(input())
print(fun2(x,y)) 

