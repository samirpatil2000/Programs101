"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""
n=600851475143
import math


def prime_factors(n):
    list=[]
    for i in range(1,int(math.sqrt(n))+1):
        if (n%i==0):
            list.append(i)
            list.append(n//i)
    return list
        # print(i)
print(list)
# list_=list.reverse()
# print(int(math.sqrt(n)))
def is_prime(n):
    return len(prime_factors(n))==2

large=0
list=prime_factors(n)
for i in range(0,len(prime_factors(n))):
    if list[i] > large and is_prime(list[i]):
        large=list[i]
print(large)
