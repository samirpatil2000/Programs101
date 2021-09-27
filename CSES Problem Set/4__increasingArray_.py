n = int(input())

arr = [int(x) for x in input().split(' ')]


def increasingArray(arr,n):
    count=0
    for i in range(1,n):
        incres=0
        if arr[i-1]>arr[i]:
            incres=arr[i-1]-arr[i]
            arr[i]+=incres
            count+=incres
    return count



 
print(increasingArray(arr,n))

        
        
        
        
        
        
        
        
        
        
        

        