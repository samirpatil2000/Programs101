
def median(arr):
    print(arr)
    if len(arr)%2==0:
        return (arr[len(arr)//2]+arr[len(arr)//2-1])//2,arr[len(arr)//2],arr[len(arr)//2-1]
    return arr[len(arr)//2]

arr=[5 ,4 ,3 ,2,1,0]

print(median(sorted(arr)))