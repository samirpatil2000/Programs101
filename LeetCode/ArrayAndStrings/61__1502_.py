def canMakeArithmeticProgression(arr):
    # arr.sorted()
    arr.sort()
    # if(len(arr)==2):
    #     return
    sum_=arr[1]-arr[0]
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i]!=sum_):
            return False
    return True


arr = [1,4]

print(arr)

print(canMakeArithmeticProgression(arr))