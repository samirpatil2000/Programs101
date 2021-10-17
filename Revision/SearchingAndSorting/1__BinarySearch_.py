class Solution:
    
    def BinarySearch(self,arr,target):
        left=0
        right=len(arr)-1
        
        while right-left>1:
            mid=(left+right)//2
            
            if arr[mid]<target:
                left=mid+1
            else:
                right=mid
        
        if arr[left]==target:return left
        if arr[right]==target:return right    
        return -1
    
    
sol=Solution()
arr,target=[2,3,4,5,6],6
print(sol.BinarySearch(arr,target))