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


# 0 , 1 , 1 , 2 , 3 , 5 ,


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
        if (num%2==0):
            sum=sum+num
            print(sum,"\n")
    return sum

print(su())




