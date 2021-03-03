def printTargetSum(arr,index,set,sum,target):
    if(index==len(arr)-1):
        if(sum==target):
            print(set)
        return
    
    printTargetSum(arr,index+1,set+str(arr[index])+",",sum+arr[index],target)
    printTargetSum(arr,index+1,set,sum,target)
    
    
list=[10,20,30,40,50]
printTargetSum(list,0,"",0,30)