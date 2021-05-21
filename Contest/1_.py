import sys

def get_ints(): 
    return map(int, sys.stdin.readline().strip().split()) 


# a,b = get_ints()
a,b = 10,15

def fun(a,b):
    count=0
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            count+=1
    return count
print(fun(a,b))



import math
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def fun(a, b):
    n = gcd(a, b) 
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
         if n % i == 0:
            if n/i == i:
                count += 1
            else:
                count += 2
    return count

print(fun(a,b))
