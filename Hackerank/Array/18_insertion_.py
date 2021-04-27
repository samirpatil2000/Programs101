
def runningTime(arr):
    # Write your code here
    count_=0
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and temp<arr[j]):
            count_+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print(count_)
    print(arr)
    return count_


arr=[2,1,3,1,2]
runningTime(arr)