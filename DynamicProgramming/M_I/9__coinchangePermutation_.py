def coinChangePermutation(coins,target):
    dp=[0 for _ in range(target+1)]
    dp[0]=1
    
    for i in range(1,len(dp)):
        for j in range(len(coins)):
            if (coins[j]<=i):
                dp[i]+=dp[i-coins[j]]
                
    
    print(dp)

class Solution():
    def coinChangeMemo(self,arr,target_sum):
        count_=[0]
        def coinMemo(arr,tar):
            if tar==0:
                count_[0]+=1
                return
            if tar<0:return
            print(tar)
            for num in arr:
                coinMemo(arr,tar-num)
            return
        coinMemo(arr,target_sum)
        print(count_)
        
count_=[0]
    
coins=[2,3,5,6]  
coinChangePermutation(coins,10)



        
            

sol=Solution()
sol.coinChangeMemo(coins,10)