class Solution:
    
    
    def isFeasible(self,arr,k,max_book):
        student=1
        sum_=0
        for i in range(len(arr)):
            if sum_+arr[i]>max_book:
                student+=1
                sum_=arr[i]
            else:
                sum_+=arr[i]
        return student<=k
                
    def minimumBookAllocation(self,arr,k):
        left=max(arr)
        right=sum(arr)
        
        result=0
        while right>=left:
            mid=(left+right)//2
            
            if self.isFeasible(arr,k,mid):
                result=mid
                right=mid-1
            else:
                left=mid+1  

        return result
    

sol=Solution()
arr,k=[10,10,20,30],2
print(sol.minimumBookAllocation(arr,k))