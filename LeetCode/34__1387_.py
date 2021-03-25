

def powerOF(n):
    count=0
    while(n!=1):
        if(n%2==0):
            n=n//2
        else:
            n=n*3+1
        count+=1
    return count

def getKTH(lo,hi,k):
    list=[]
    for i in range(lo,hi+1):
        list.append(powerOF(i))
    list.sort()
    return list


lo = 12
hi = 15
k = 2
print(getKTH(lo,hi,k))

    


# print(powerOF(12))