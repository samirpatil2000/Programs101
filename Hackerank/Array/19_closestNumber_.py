
def closestNumber(arr):
    print(arr)
    min_diff=2**32
    count=0
    list_=[]
    for i in range(0,len(arr)-1):
        # print(arr[i+1],arr[i])˜
        if arr[i+1]-arr[i] <= min_diff:
            if arr[i+1]-arr[i]==min_diff:
                count+=1
                list_.append(arr[i])
                list_.append(arr[i+1])
            else:
                list_.clear()
                min_diff=arr[i+1]-arr[i]
                list_.append(arr[i])
                list_.append(arr[i+1])
                count=1
    return count,list_
            
            

# arr=[-20, -3916237, -357920, -3620601, 7374819, -7330761, 30 ,6246457, -6461594 ,266854]
arr=[5 ,4 ,3 ,2]
# print(closestNumber(arr))
print(closestNumber(sorted(arr)))




