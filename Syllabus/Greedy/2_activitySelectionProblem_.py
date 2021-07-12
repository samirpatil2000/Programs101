

a=[
    [10,20],
    [20,30],
    [10,15],
    [25,30],
    [15,25],
    ]
def maxActivityCount(arr):
    arr.sort(key=lambda arr:arr[1])
    
    counter_=1
    end_at=arr[0]
    for i in range(1,len(arr)):
        if arr[i][0]>=end_at[1]:
            counter_+=1
            end_at=arr[i]
    return counter_


print(maxActivityCount(a))