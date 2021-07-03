from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        arr=[0,1]
        if n==1:return arr
        
        for i in range(1,n):
            N=2**i
            j=len(arr)-1
            while j>=0:
                arr.append(N+arr[j])
                j-=1
        return arr
sol=Solution()
n=16
print(sol.grayCode(n))