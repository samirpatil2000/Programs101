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
        return dp[-1]
    def numDecodings2(self, s: str) -> int:
        dp=[0]*len(s)
        dp[0]=1
        if s[0]=="0":dp[0]=0
        for i in range(1,len(s)):
            ch1=int(s[i-1])
            ch2=int(s[i])
            if ch1==0 and ch2==0:
                dp[i]=0
            elif ch1==0 and ch2!=0:
                dp[i]=dp[i-1]
            elif ch1!=0 and ch2==0:
                if ch1<=2:
                    if i-2>=0:
                        dp[i]=dp[i-2]
                    else:
                        dp[i]=1
                else:
                    dp[i]=0
            else:
                if int(str(ch1)+str(ch2))<=26:
                    if i-2>=0:
                        dp[i]=dp[i-1]+dp[i-2]
                    else:
                        dp[i]=dp[i-1]+1
                else:
                    dp[i]=dp[i-1]
        return dp[-1]
                    
                
sol=Solution()
s="2263322333410"
print(sol.numDecodings(s))
print(sol.numDecodings2(s))