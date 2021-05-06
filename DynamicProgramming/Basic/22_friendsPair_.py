
def rec(output_,str_):
    if len(str_)==0:
        print(output_)
        return

    ch=str_[0]
    if len(output_)!=0:
        rec(ch+"-"+output_,str_[1:])
    else:
        rec(ch,str_[1:])
    for i in range(1,len(str_)):
        if len(output_)!=0:
            rec(ch+str_[i]+"-"+output_,str_[1:i]+str_[i+1:])
        else:
            rec(ch+str_[i],str_[1:i]+str_[i+1:])
            
count_=0
def count_pairs(n):
    global count_
    if n==0:
        count_+=1
        return
    count_pairs(n-1)
    for i in range(1,n):
        count_pairs(n-2)
        # s=
        

def count_pairs_(n):
    if n==0 or n==1 or n==2:
        return n
    count_2=count_pairs_(n-1)
    for i in range(1,n):
        count_2+=count_pairs_(n-2)
    return count_2


def count_pairs_dp_arr(n,dp):
    if n==0 or n==1 or n==2:
        return n
    if dp[n-1]:
        count_2=dp[n-1]
    else:
        count_2=count_pairs_dp_arr(n-1,dp)
        
    # for i in range(1,n):
    #     if dp[n-2]:
    #         count_2+=dp[n-2]
    #     else:
    #         count_2+=count_pairs_dp_arr(n-2,dp)
    if dp[n-2]:
        count_2+=(dp[n-2])*(n-1)
    else:
        count_2+=(count_pairs_dp_arr(n-2,dp))*(n-1)
    
    
    return count_2
    
str_="1234567"
rec("",str_)
count_pairs(len(str_))
print(count_)
print(count_pairs_(len(str_)))

dp=[None for _ in range(len(str_)+1)]
print(count_pairs_dp_arr(len(str_),dp))


    

#using DP
def friendPair(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,len(dp)):
        dp[i]=dp[i-1]+dp[i-2]*(i-1)
        
    print(dp)

# friendPair(5)
        