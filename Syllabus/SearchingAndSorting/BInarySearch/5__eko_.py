

class Solution:
    
    
    def isFeasible(self,arr,height,M):
        sum_=0
        for i in range(len(arr)):
            if height<=arr[i]:
                sum_+=(arr[i]-height)
        print(height,sum_)
        if sum_>=M:
            return True
        return False
                
    def eko(self,arr,M):
        left=0
        right=max(arr)
        
        # we can take this one also
        # right=1e9+10
        
        result=0
        while right-left>1:
            mid=(left+right)//2
            
            if self.isFeasible(arr,mid,M):
                result=mid
                
                left=mid
            else:
                right=mid-1
        if self.isFeasible(arr,right,M):
            return right
        
        return result,left
    

sol=Solution()
arr,M=[10,20,15,17],7
print(sol.eko(arr,M))