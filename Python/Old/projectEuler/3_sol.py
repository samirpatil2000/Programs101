
#if you had some trouble getting the number into a variable //see the note at the end on page 2.
n=600851475143

import time
import math

t1=time.perf_counter()
def prime(n):
    factor = 2
    lastFactor = 1
    list=[]
    while n>1:
        # print("factor = ",factor)
        # print("n = ",n)
        if n % factor==0:
            lastFactor=factor
            n=n / factor
            list.append(factor)
            # print("Before while n = ",n)
            while n % factor==0:
                n=n / factor
        factor=factor+1
            # print("factor = ",factor)
            # print("After while n = ",factor)
    return list

print("and this last factor",prime(n))
t2=time.perf_counter()
print(f"time of fun 1 is {t2-t1}")


"""This works for the given number, but can be improved in several ways.
First of all: 2 is the only even prime, so if we treat 2 separately we can increase factor with 2 every step."""

def prime_(n):
    factor = 3
    lastFactor = 1
    list=[]

    if (n%2==0):
        n=n/2
        list.append(2)
        while n%2==0:
            n=n/2
        else:
            lastFactor=1

    while n>1:
        if n % factor==0:
            lastFactor=factor
            n=n / factor
            list.append(factor)
            while n % factor==0:
                n=n / factor
        factor=factor+2
    return list

print("and this last factor",prime_(n))
t3=time.perf_counter()
print(f"time of fun 2 is {t3-t2}")



def prime__(n):
    factor = 3
    lastFactor = 1
    list=[]
    max_factor=int(math.sqrt(n))

    if (n%2==0):
        n=n/2
        list.append(2)
        while n%2==0:
            n=n/2
        else:
            lastFactor=1

    while n>1: #and factor<=max_factor:
        if n % factor==0:
            lastFactor=factor
            n=n / factor
            list.append(factor)
            while n % factor==0:
                n=n / factor
            max_factor = int(math.sqrt(n))
        factor=factor+2
    return list

print("and this last factor",prime__(n))
t4=time.perf_counter()
print(f"time of fun 3 is {t4-t3}")