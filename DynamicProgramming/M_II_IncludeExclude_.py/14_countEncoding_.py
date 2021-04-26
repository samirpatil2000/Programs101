

def countEncoding(string_):
    dp=[0]*(len(string_))
    # print(dp)
    dp[0]=1
    for i in range(1,len(dp)):
        ch1,ch2=int(string_[i-1]),int(string_[i])
        
        if ch1==0 and ch2==0:
            dp[i]=0
        elif ch1==0 and ch2!=0:
            dp[i]=dp[i-1]
        elif ch1!=0 and ch2==0:
            print(int(str(ch1)+str(ch2)))
            if int(str(ch1)+str(ch2))<=26:
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
                    dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]
    return dp
                

print(countEncoding('21123'))