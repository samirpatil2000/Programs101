def selfDividing(left,right):
    list_=[]
    for i in range(left,right+1):
        
        num_=str(i)
        j=len(num_)-1
        while(j>=0):
            if(int(num_[j])==0):
                break
            if(i%int(num_[j])==0):
                j-=1
                continue
            break
        if(j==-1):
            # print(i)
            list_.append(i)    
    return list_

print(selfDividing(1,22))