# s = "Gunjan"
# print(s[2:])
# print(s[4:len(s)])
# print(s[0:10])
# change hello to help!
# s="hello"
# s=s[0:3]+"p!"
# print(s)

# def primeNumber(n):
#     list = []
#
#     for i in range (0,n+1):
#         for j in range(1,i+1):
#             if (n%j == 0):
#                 list.append(j)
#
#         return list
#
#
# print(primeNumber(24))

def factor(n):
    factors=[]
    for i in range(1,n+1):
        if (n%i==0):
            factors.append(i)
    return factors

def isprime(n):
    return (factor(n)==[1,n])


def primeUpto(n):
    listOfPrime=[]
    for i in range(1,n+1):
        if isprime(i):
            listOfPrime.append(i)
    return (listOfPrime)

print(primeUpto(102))





#print(factor(24))




