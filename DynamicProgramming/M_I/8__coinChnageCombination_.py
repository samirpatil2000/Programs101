

def coinChangeCombi(coin_arr,target_num):
    dp=[0 for _ in range(target_num+1)]
    dp[0]=1
    for i in range(len(coin_arr)):
        for j in range(coin_arr[i],len(dp)):
            dp[j]+=dp[j-coin_arr[i]]
    
    print(dp)
    

    
arr=[2,3,5]
coinChangeCombi(arr,7)