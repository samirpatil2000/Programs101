import bisect
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
            
    
    def longestIncresingSubSequence_NlogN(self,arr):
        dp=[2**32]*(len(arr)+1)
        dp[0]=0
        
        print(bisect.bisect(arr,10))
        
        
        # for ele in arr:
        #     indx=bisect.bisect(arr,ele)
        #     dp[indx]=ele
        #     print(dp,indx,ele)
    
            
            
        
        
        
    
sol=Solution()
arr=[10,22,9,33,21,50]
arr=[10,9,2,5,3,7,101,18]

x=[10, 2**32, 2**32, 2**32, 2**32, 2**32, 2**32, 2**32, 2**32]
print(bisect.bisect(x,9))

# print(sol.longestIncresingSubSequence(arr))
# print(sol.longestIncresingSubSequenceTabulation(arr))
            
            
print(sol.longestIncresingSubSequence_NlogN(arr))