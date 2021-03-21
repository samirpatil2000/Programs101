def merge(nums1, m, nums2, n):
    
    # print(i)
    for j in range(n):
        i=m-1+j
        print(i,j)
        while(i >= 0 and nums1[i]>=nums2[j]):
            nums1[i+1]=nums1[i]
            i-=1
        nums1[i+1]=nums2[j]
            
# nums1 = [2,0] #[1,2,3,0,0,0]
# m = 1 #3
# nums2 =[1] # [2,5,6] 
# n = 1 #3


nums1 = [1,2,3,0,0,0]
m = 3
nums2 =[2,5,6] 
n = 3


merge(nums1,m,nums2,n)
print(nums1)