class Solution:
    def maxiumSumIncresingSubSequenceTabulation(self,arr):
        dp=[0]*(len(arr))
        dp[0]=arr[0]
        for i in range(1,len(arr)):
            max_=0
            for j in range(i,-1,-1):
                if arr[i]>arr[j]:
                    max_=max(max_,dp[j])
            dp[i]=max_+arr[i]
        return dp
            
        
    
sol=Solution()
arr=[10,22,9,33,21,50,41,60,80,3]
print(sol.maxiumSumIncresingSubSequenceTabulation(arr))
            
            
        