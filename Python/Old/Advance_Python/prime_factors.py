import math


num=600851475143


def factors_only(n):
    list = []
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            list.append(i)
    return list

# print(factors_only(num))

def prime_factors(n):
    list=[]
    # while n > 1 :
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            list.append(i)
            n=n / i
            # print(n)
            # print(i)

    return list

print(prime_factors(num))





"""THIS IS THE CORREST APPROACH ALTHOUGH """
def prime_factors_2(n):
    list=[]
    divisior=2
    lastfactor=divisior
    while divisior <= n  :
            if (n%divisior==0):
                list.append(divisior)
                n=n / divisior
                lastfactor = divisior
                while n%divisior==0:
                    n=n/divisior
            divisior+=1
                # print(n)
                # print(divisior)
            # else:
            #     divisior+=1
    return list

print(prime_factors_2(num))


