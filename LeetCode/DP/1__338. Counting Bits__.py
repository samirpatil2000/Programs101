from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[""]*(n+1)
        dp[0]="0"
        dp[1]="1"
        
        # def helper(n:str)->str:
        #     if n=="0" or n=="1":return n
        #     x=bin(int("1",2)+int(helper(str(int(n)-1)),2))[2:]
        #     dp[int(n)]=x
        #     return x
        
        for i in range(2,len(dp)):
            dp[i]=bin(int("1",2)+int(dp[i-1],2))[2:]
            
        for i in range(len(dp)):
            dp[i]=dp[i].count("1")
        return dp
    

        
sol=Solution()
print(sol.countBits(5))
        