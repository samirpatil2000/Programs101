class Solution:
    def logestIncresingSubSequenceTabulation(self,arr):
        dp=[0]*(len(arr))
        dp[0]=1
        for i in range(1,len(arr)):
            max_=0
            for j in range(i,-1,-1):
                if arr[i]>arr[j]:
                    max_=max(max_,dp[j])
            dp[i]=max_+1
        return dp
    
    def logestDecreasingSubSequenceTabulation(self,arr):
        dp=[0]*(len(arr))
        dp[-1]=1
        for i in range(len(arr)-1,-1,-1):
            max_=0
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    max_=max(max_,dp[j])
            dp[i]=max_+1
        return dp
    
    def longestBotonic(self,arr):
        incr=self.logestIncresingSubSequenceTabulation(arr)
        decr=self.logestDecreasingSubSequenceTabulation(arr)
        max_=0
        for i in range(len(arr)):
            max_=max(max_,incr[i]+decr[i])
        return max_-1
    
    
    
        
        
    
sol=Solution()
arr=[10,22,9,33,21,50,41,60,80,3]
print(sol.longestBotonic(arr))
            
            
        