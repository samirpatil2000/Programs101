
def merge(arr,left,mid,right):
    k=0
    i=left
    j=mid+1
    b=[0]*len(arr)
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            b[k]=arr[i]
            i+=1
        else:
            b[k]=arr[j]
            j+=1
        k+=1
    if(i>mid):
        while(j<=right):
            b[k]=arr[j]
            j+=1
            k+=1
    if(j>right):
        while(i<=mid):
            b[k]=arr[i]
            i+=1
            k+=1
    i=left
    j=0
    while(j<=k):
        arr[i]=b[j]
        i+=1
        j+=1

def mergeSort(arr,left,right): 
	if left < right: 
		mid = (left+right)//2

		mergeSort(arr, left, mid) 
		mergeSort(arr, mid+1, right) 
		merge(arr, left, mid, right) 

arr=[3,1,235,5,56,32,33,21,1]
mergeSort(arr,0,len(arr)-1)
print(arr)

    