from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        # def dfs(s):
        #     if s!="" and int(s)>n:
        #         return 0
        #     else:
        #         x=0
        #         for i in digits:
        #             num=int(s+i)
        #             if num<=n:
        #                 print(num)
        #                 x+=(dfs(str(num))+1)
        #         return x
        ans=0
        m=len(digits)
        s=str(n)
        for i in range(1,len(s)):
            ans+=(m**i)
        print(ans)
        for i in range(len(s)):
            hasSameNo=False
            for d in digits:
                d=int(d)
                if d<int(s[i]):
                    x=len(s)-i-1
                    ans+=(m**x)
                elif d==int(s[i]):
                    hasSameNo=True
                    if i==len(s)-1:
                        ans+=1
            if not hasSameNo:
                return ans
            
            
                    
        return ans

sol=Solution()
digits = ["1","3","5","7"]
n = 100

digits = ["1","4","9"]
n = 1000000000

digits = ["7"]
n = 8

digits=["3","4","8"]
n=4

# digits,n=["5","6"],19
print(sol.atMostNGivenDigitSet(digits,n))
            