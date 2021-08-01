

class Solution:
    def countDistinctSubSequnce(self,s:str)->int:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            dp[i]=2*dp[i-1]
            for j in range(i-1,0,-1):
                if s[i-1]==s[j-1]:
                    dp[i]-=dp[j-1]
        return dp
sol=Solution()

print(sol.countDistinctSubSequnce("abcbae"))
                
            
        