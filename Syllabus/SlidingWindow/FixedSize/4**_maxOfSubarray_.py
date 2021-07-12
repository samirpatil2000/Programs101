

def maxFunction(arr,k):
    queue=[0]
    new_arr=[None for _ in range(len(arr)-k)]
    for i in range(1,k):
        while(len(queue)>0 and arr[i]>arr[queue[0]]):
            queue.pop(0)
        queue.append(i)
        
        
    print(queue)
        
    for i in range(len(arr)-k):
        while(len(queue)>0 and arr[i+k]>arr[queue[0]]):
            queue.pop(0)
        queue.append(i+k)
        new_arr[i]=arr[queue[0]]
        if(queue[0]==i):
            queue.pop(0)
    
    return new_arr



arr=[2,3,1,5,7,6,4,8]
# print(arr.pop(0))
k=3
print(maxFunction(arr,k))
        
            
            
    