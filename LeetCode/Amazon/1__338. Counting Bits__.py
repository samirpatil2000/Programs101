from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            ans.append(bin(i)[2:].count('1'))
        return ans
    
    def countBitsDP(self, n: int) -> List[int]:
        # property of binary number
        dp=[]
        dp.append(0)
        dp.append(1)
        for i in range(2,n+1):
            if i%2==1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp
    
sol=Solution()
print(sol.countBits(10))

print(sol.countBitsDP(10))