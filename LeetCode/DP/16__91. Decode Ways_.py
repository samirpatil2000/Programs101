class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*len(s)
        dp[0]=1
        if s[0]=="0":dp[0]=0
        for i in range(1,len(s)):
            ch1=s[i-1]
            ch2=s[i]
            if int(ch1)==0 and int(ch2)==0:
                dp[i]=0
            elif int(ch1)==0 and int(ch2)!=0:
                dp[i]=dp[i-1]
            elif int(ch1)!=0 and int(ch2)==0:
                if int(ch1)==1 or int(ch1)==2:
                    if i-2>=0:
                        dp[i]=dp[i-2]
                    else:
                        dp[i]=1
                else:
                    dp[i]=0
            else:
                if int(ch1+ch2)<=26:
                    if i-2>=0:
                        dp[i]=dp[i-1]+dp[i-2]
                    else:
                        dp[i]=dp[i-1]+1
                else:
                    dp[i]=dp[i-1]
        return dp
                    
                
sol=Solution()
s="10"
print(sol.numDecodings(s))