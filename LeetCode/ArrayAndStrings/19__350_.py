def find(nums_1,nums_2):
    list_=[]
    nums_1=sorted(nums_1)
    nums_2=sorted(nums_2)
    i=j=0
    while(i<len(nums_1) and j<len(nums_2)):
        if(nums_2[j]==nums_1[i]):
            list_.append(nums_1[i])
            i+=1
            j+=1
        else:
            if(nums_1[i]>nums_2[j]):
                j+=1
            else:
                i+=1
    return list_


nums1 = [1,2,2,1]
nums2 = [2,2]

print(find(nums1,nums2))