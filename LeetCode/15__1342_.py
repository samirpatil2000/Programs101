def numberOfSteps(num):
    count=0
    while(num>0):
        # print(num)
        if(num%2==0): #odd
            num=num//2
        else:
            num=num-1
        count+=1
    return count

print(numberOfSteps(8))
            
            