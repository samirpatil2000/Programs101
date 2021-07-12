
def knapsack(values,weights,n,target):
    dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
    
    for row in range(1,n+1):
        for col in range(1,target+1):
            val=values[row-1]
            dp[row][col]=dp[row-1][col]
            if(col>=val):
                dp[row][col]=max(dp[row-1][col],weights[row-1]+dp[row-1][col-val])
                    
    
    print(dp[-1][-1])
    
    
    
class Solution():
    
    def knapsack(self,arr,wt,cap_max):
        max_=[0]
        def rec(arr,wt,index,cap_max,wsf,csf,memo={}):
            if index>=len(arr):return
            if csf>cap_max:return
            if csf==cap_max:
                if max_[0]<wsf:max_[0]=wsf 
                return
            # print(max_[0],wsf,csf)
            rec(arr,wt,index+1,cap_max,wsf+wt[index],csf+arr[index])
            rec(arr,wt,index+1,cap_max,wsf,csf)
        rec(arr,wt,0,cap_max,wt[0],arr[0])
        return max_[0]
    def withMemo(self,arr,wt,cap_max,index,csf):
        if index>=len(arr):return None
        if csf>cap_max:return None
        if csf==cap_max:
            return 0
        with__list=self.withMemo(arr,wt,cap_max,index+1,csf+arr[index])
        without_list=self.withMemo(arr,wt,cap_max,index+1,csf)
        print(without_list,with__list,index,csf)
        if with__list!=None and without_list!=None:
            return max(with__list+wt[index],without_list)
        if with__list!=None:
            return with__list+wt[index]
        if without_list!=None:
            return without_list
        
            
        
arr=[2,5,1,3,4]
wt=[15,14,10,45,30]   
    
knapsack(arr,wt,len(arr),7)
sol=Solution()
print(sol.knapsack(arr,wt,7))
print(sol.withMemo(arr,wt,7,0,arr[0]))
    