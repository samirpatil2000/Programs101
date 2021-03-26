

def powerOF(n):
    count=0
    while(n!=1):
        if(n%2==0):
            n=n//2
        else:
            n=n*3+1
        count+=1
    return count


def smallNumber(list_,start):
    small=list_[start][0]
    pos=start
    for start in range(start+1,len(list_)):
        if(list_[start][0]==small):
            if (list_[start][1]>list_[pos][1]):
                small=list_[pos][0]
                pos=pos
            else:
                small=list_[start][1]
                pos=start
        elif(list_[start][0]<small):
            small=list_[start][0]
            pos=start
    return pos
            

def selectionSortTechanic(list_,k):
    for i in range(k):
        pos=smallNumber(list_,i)
        temp=list_[i]
        list_[i]=list_[pos]
        list_[pos]=temp
    return list_
        
    
    

def getKTH(lo,hi,k):
    list=[]
    for i in range(lo,hi+1):
        list.append([powerOF(i),i])
    print(list)
    # list=selectionSortTechanic(list,k)
    list.sort()
    print(list)
    return list[k-1]

lo = 10
hi = 20
k = 5

print(getKTH(lo,hi,k))

    


# print(powerOF(12))