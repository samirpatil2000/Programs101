class Solution:
    def longestIncresingSubSequence(self,arr):
        result=[]
        def rec(arr,index,suq_so_far,memo={}):
            if index>len(arr):
                return
            if index==len(arr):
                result.append(suq_so_far)
                return
            
            rec(arr,index+1,suq_so_far,memo)
            
            if not suq_so_far:
                rec(arr,index+1,suq_so_far+[arr[index]],memo)
            elif suq_so_far[-1]<=arr[index]:
                rec(arr,index+1,suq_so_far+[arr[index]],memo)
            
        rec(arr,0,[])
        return result

    # def longestIncresingSubSequenceMemo_(self,arr):
        
    #     def rec(arr,index,prev_,memo={}):
    #         if index>=len(arr):
    #             return
    #         # if index==len(arr)-1:
    #         #     return [[]]
            
    #         # result=[]
    #         # x=rec(arr,index+1,prev_,memo)
           
            
    #         # if prev_>=arr[index]:
    #         #     if x: 
    #         #         result.append(x.append(arr[index]))                
                
                
    #         #     result.append(y.append(arr[index]))
            
    #     # rec(arr,0,[])
    #     return 
    def longestIncresingSubSequenceTabulation(self,arr):
        dp=[0]*(len(arr))
        dp[0]=1
        for i in range(1,len(arr)):
            max_=0
            for j in range(i,-1,-1):
                if arr[i]>arr[j]:
                    max_=max(max_,dp[j])
            dp[i]=max_+1
        return dp
            
        
    
sol=Solution()
arr=[10,22,9,33,21,50]
print(sol.longestIncresingSubSequence(arr))
print(sol.longestIncresingSubSequenceTabulation(arr))
            
            
        