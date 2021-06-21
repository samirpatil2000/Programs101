from typing import List


class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        if len(arr)==1:return arr[0]
        maxVal=arr[0]
        minVal=arr[0]
        ans=arr[0]
        for i in range(1,len(arr)):
            tempMax=maxVal
            maxVal=max(maxVal*arr[i],arr[i],minVal*arr[i])
            minVal=min(tempMax*arr[i],arr[i],minVal*arr[i])
            ans=max(ans,maxVal)
        return ans
    
sol=Solution()
arr=[1,2,-1,-2,2,1,-2,1,4,-5,4]
print(sol.maxProduct(arr))
            