
def rec(n,output_,str_):
    if n==3:
        print(output_)
        return

    ch=str_[0]
    rec(n+1,ch+"-"+str_[1:])
    for i in range(2,len(str_)):
        # print(str_[1:i-1]+str_[i:],str_)
        rec(n+1,ch+str_[i-1]+"-"+str_[1:i-1]+str_[i:])
        

    
    
str_="123"
rec(0,"",str_)

print(str_[1:])

# str_="12345"
# print(str_[:1])
# for i in range(1,len(str_)):
#     print(str_[:i-1],str_[i:],str_[i])
    


def friendPair(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,len(dp)):
        dp[i]=dp[i-1]+dp[i-2]*(i-1)
        
    print(dp)

# friendPair(5)
        