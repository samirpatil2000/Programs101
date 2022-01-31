def factor(n):
    list=[]
    for i in range(1,n+1):
        if (n%i==0):
            list.append(i)
    return list

def isprime(n):
    return (factor(n)==[1,n])

def uptoprime(n):
    list=[]
    i=1
    counter=0
    while(counter<n):
        if isprime(i):
            list.append(i)
            counter=counter+1
        i = i + 1

    return list

print(uptoprime(20))
