arr=[
    [1,3.00],
    [2,3.76],
    [3,3.54],
    [4,3.31],
    [5,3.32],
    [1,3.38]
    ]
x=sorted(arr,key=lambda arr:arr[1])
print(x)
# arr.sort(key=lambda arr:arr[0])
print(arr)

arr.sort(key=lambda arr:arr[0]/arr[1],reverse=True)

