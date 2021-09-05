#!/bin/python3



# t = int(input().strip())


# def function(n:int)->int:
#     sum_=0
#     for i in range(1,n):
#         if i%3==0 or i%5==0:  
#             sum_+=i
#             print(i)
#     return sum_
# for a0 in range(t):
#     n = int(input().strip())
print(function(10))

def sum_(n, k):
    d = n // k
    return k * (d * (d+1)) // 2
def function(n):
    return sum_(n, 3) + sum_(n, 5) - sum_(n, 15)

t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(function(N - 1)) # below N