

    

def pick(arr):
    max_len=0
    i=0
    while(i<len(arr)-1):
        j=i+1
        
        while(j<len(arr) and diffChecker(arr,left=i,right=j-1,element=arr[j])):
            print(arr[i:j],arr[j])
            j+=1
        if max_len<(j-i+1):
            max_len=j-i+1
        if j<len(arr)-1:
            i=j+1
        else:
            return max_len
    return max_len

def diffChecker(arr,left,right,element):
    for i in range(left,right+1):
        if abs(element-arr[i])<=1:
            return True

arr=[1 ,2, 2, 3, 1, 2]
print(pick(arr))
    