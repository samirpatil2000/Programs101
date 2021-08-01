def getUnique(arr):
    i=0
    count=0
    while(i<len(arr)):
        print(count ,i )
        while(i<len(arr)-1 and arr[i]==arr[i+1]):
            i+=1
        arr[count]=arr[i]
        i+=1
        count+=1
    return arr[:count]


def intersection(nums1, nums2):
    if(len(nums1)==0 or len(nums2)==0):
        return []
    list_=[]
    nums1=sorted(nums1)
    nums2=sorted(nums2)
    i=j=0
    while(i<len(nums1) and j<len(nums2)):
        if(nums2[j]>nums1[i]):
            i+=1
        elif(nums2[j]<nums1[i]):
            j+=1
        else:
            list_.append(nums1[i])
            i+=1
            j+=1
    return getUnique(list_)

nums1 = []
nums2 = []
print(intersection(nums1,nums2))

a=[2,2,3,3,4,5,5,5,6]
print(getUnique(a))
    