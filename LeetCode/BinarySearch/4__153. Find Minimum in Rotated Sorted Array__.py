from typing import List


class Solution:
    def Search(self,arr:List[int])->int:
        n=len(arr)
        left,right=0,n-1
        
        while left<right:
            mid=(right+left)//2
            if arr[right]>=arr[mid]:
                right=mid
            else:
                left=mid+1
        return arr[left]
sol=Solution()
print(sol.Search())