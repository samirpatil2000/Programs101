

def decodes_ways(s):
    dp = [0]*(len(s)+1)
    dp[0] = 1

    if s[0]=='*':
        dp[1] = 9
    elif s[0]!='0':
        dp[1] = 1

    for i in range(2,len(s)+1):

        # think about 1-1 chars
        if s[i-1] == '*':
            dp[i] = 9*dp[i-1]
            if s[i-2]=='1':
                dp[i] += 9*dp[i-2]
            elif s[i-2] == '2':
                dp[i] += 6*dp[i-2]
            elif s[i-2] == '*':
                dp[i] += (9*dp[i-2] + 6*dp[i-2])
        elif s[i-1] !='0':
            dp[i] += dp[i-1]

        # think about 2-2 chars
        if s[i-1]!='*':
            if s[i-2] == '1' or ( s[i-2] == '2' and s[i-1] < '7' ):
                dp[i] += dp[i-2]
            elif s[i-2]=='*':
                if s[i-1]<'7':
                    dp[i] += 2*dp[i-2]
                else:
                    dp[i] += dp[i-2]

    return dp[-1]%(10**9+7)
    
class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        dp[0]=1
        if s[0]=='*':
            dp[1]=9
        elif s[0]!='0':
            dp[1]=1
        
        for i in range(2,len(s)+1):
            ch1=s[i-2]
            ch2=s[i-1]
            
            if ch2=='*':
                dp[i]=9*dp[i-1]
                if ch1=='1':
                    dp[i]+=9*dp[i-2]
                elif ch1=='2':
                    dp[i]+=6*dp[i-2]
                elif ch1=='*':
                    dp[i]+=15*dp[i-2]
            elif ch2!='0':
                dp[i]=dp[i-1]
            
            if ch2!='*':
                
                if ch1=='*':
                    if int(ch2)<=6:
                        dp[i]+=2*dp[i-2]
                    else:
                        dp[i]+=dp[i-2]
                elif ch1 == '1' or ( ch1 == '2' and ch2 < '7' ):
                    # print("@")
                    dp[i]+=dp[i-2]
                
        return dp[-1]%(10**9+7)
    
sol=Solution()
s="104"
print(sol.numDecodings(s),decodes_ways(s))
                
                    
                    