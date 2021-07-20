class Solution:
    
    def maxOverLappingBridge(self,arr):
        arr.sort(key=lambda x:x[0])
        dp=[0]*(len(arr))
        dp[0]=1
        for i in range(1,len(arr)):
            max_=0
            for j in range(i,-1,-1):
                if arr[i][1]>=arr[j][1]:max_=max(max_,dp[j])
            dp[i]=max_+1
        return dp[-1]
    
    
    
    

    
sol=Solution()
arr=[[10,20],[2,7],[8,15],[17,8],[21,40],[50,4],[41,57],[60,80],[80,90],[1,30]]

print(sol.maxOverLappingBridge(arr))

            
            
        