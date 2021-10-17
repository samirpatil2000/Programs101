

class Solution:
    
    
    def canPlaceCows(self,arr,minDist,cows):
        last_cow=-1
        for i in range(len(arr)):
            if last_cow==-1 or arr[i]-last_cow>=minDist:
                last_cow=arr[i]
                cows-=1
            if cows==0:
                return True
        return cows==0
                
                
    def eko(self,arr,cows):
        left=0
        right=max(arr)
        
        # we can take this one also
        # right=1e9+10
        
        result=0
        while right-left>1:
            mid=(left+right)//2
            
            if self.canPlaceCows(arr,mid,cows):
                result=mid
                
                left=mid
            else:
                right=mid-1
        if self.canPlaceCows(arr,right,cows):
            return right
        
        return result,left
    

sol=Solution()
arr,cows=[1,2,4,8,9],3
print(sol.eko(arr,cows))