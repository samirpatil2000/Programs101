class Solution:
    
    def lowerBound(self,arr,ele):
        low=0
        high=len(arr)-1
        while high-low>1:
            mid=(low+high)//2
            if arr[mid]<ele:
                low=mid+1
            else:
                high=mid
        if arr[low]>=ele:return low
        if arr[high]>=ele:return high
        return -1
    
    def upperBound(self,arr,ele):  # matlab ele is just bada number
        low=0
        high=len(arr)-1
        while high-low>1:
            mid=(low+high)//2
            if arr[mid]<=ele:
                low=mid+1
            else:
                high=mid
        if arr[low]>ele:return low
        if arr[high]>ele:return high
        return -1

sol=Solution()
arr,ele=[1,3,4,6,8],5
print(sol.lowerBound(arr,ele))

print(sol.upperBound(arr,ele))
        