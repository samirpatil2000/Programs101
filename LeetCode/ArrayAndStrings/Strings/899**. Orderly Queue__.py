class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return "".join(sorted(s))
        else:
            ans=s
            for i in range(1,len(s)):
                print(s[i:]+s[:i],ans)
                ans=min(s[i:]+s[:i],ans)
                print(ans)
                
        return ans
    
sol=Solution()
s = "baaca"

k = 1
print(sol.orderlyQueue(s,k))