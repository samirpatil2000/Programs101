


def firstNew(arr,k):
    n=len(arr)
    queue=[]
    for i in range(k):
        if(arr[i]<0):
            queue.append(i)
    new_arr=[None for _ in range(n-k)]
    for i in range(n-k):            
        if(len(queue)!=0 and queue[0]<=i+k):
            new_arr[i]=arr[queue[0]]
            print(queue[0],i)
            if(queue[0]==i):
                queue.pop(0)
                print(queue)
        else:
            new_arr[i]=0
        if(arr[i+k]<0):
            queue.append(i+k)
            print(arr[i+k],i+k)
    return new_arr


list_=[12,-1,0,-7,8,-15,30,16,28]
k=2
print(firstNew(list_,k))
            
        