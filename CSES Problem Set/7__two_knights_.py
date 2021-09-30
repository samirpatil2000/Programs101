n=int(input())
# import math
# n=8

def fun(n:int):
    print(0)
    for i in range(2,n+1):
        print(int(i * i * (i * i - 1) / 2 - 4 * (i - 1) * (i - 2)))
fun(n)