# def _sum(self,arr, n):
#     addition=0
#     for element in arr:
#         addition= addition + element
#     return additionclass

# arr=[2,3,4,5,6,6,6,6,6]
# x=6
# counter=0
# for i in arr:
#     if arr[i] == x:
#         counter=+1
#         break
# print(counter)


# 0 , 1 , 1 , 2 , 3 , 5 ,8, 13 , 21 , 34
import time

t1=time.perf_counter()

def fib(n):
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n - 2)
# print(fib(10))


def fib_iterative(n):
    a=0
    b=1
    c=0

    if n==1:
        return 0
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c

# print(fib_iterative(10))
def su():
    i=0
    sum = 0
    while(sum<4000000):
        i=i+1
        num=fib_iterative(i)
        print(num)
        if (num%2==0):
            sum=sum+num
            print("Sum is ",sum,"\n")
    return sum

print(su())

t2=time.perf_counter()

print(f'FINISHED IN {t2-t1}')


def iterative_():
    a1=0
    b1=1
    summed=0

    while(summed<4000000):
        z=(a1+b1)
        if (z%2==0):
            summed=summed+z
        a1=b1
        b1=z
    return summed

print(iterative_())
t3=time.perf_counter()
print(f'FINISHED IN {t3-t2}')




"""TRY TO PRINT ONLY EVEN NUMBERS    Faster method """
""" We know that every 3rd number is even """

# 1 , 1 , -- 2 , 3 , 5 , -- 8, 13 , 21 , -- 34
"""
1 1 2 3 5 8 13 21 34 55 89 144 ... 
a b c a b c  a  b  c  a  b  c
"""

def iterative_even():
    a=1
    b=1
    c=a+b
    summed=0

    while(summed<4000000):

        a=b+c
        b=c+a
        c = (a + b)
        summed += c

    return summed

print("throught direct even",iterative_even())
t4=time.perf_counter()
print(f'FINISHED IN {t4-t3}')