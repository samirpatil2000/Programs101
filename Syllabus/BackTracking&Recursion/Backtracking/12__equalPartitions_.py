from typing import List


class Solution:
    def partions(self,arr,k):
        
        target=sum(arr)//k
        def dfs(index,subsets:List[int]):
            if index==len(arr):
                if len(set(subsets))==1 and subsets[0]==target:
                    print(subsets)
                return
            for i in range(len(subsets)):
                if subsets[i]>0:
                    if subsets[i]+arr[index]<=target:    
                        subsets[i]+=arr[index]
                        dfs(index+1,subsets)
                        subsets[i]-=arr[index]
                else:
                    subsets[i]+=arr[index]
                    dfs(index+1,subsets)
                    subsets[i]-=arr[index]
                    break
                    
            
        subsets=[0]*k
        dfs(0,subsets)    
        
        
sol=Solution()
arr,k=[9,4,5,9],3
print(sol.partions(arr,k))
        

