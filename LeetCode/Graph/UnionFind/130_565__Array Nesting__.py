from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited={}
        self.max_=0
        def find(i,total,visited):
            if i in visited:
                self.max_=max(self.max_,total)
                return
            visited.add(i)
            find(nums[i],total+1,visited)
        for i in nums:
            if i not in visited:
                find(i,0,visited)
        return self.max_
    
    
    
                
                
        
        
        
        
        
    #     parent=[-1]*(len(nums))
    #     self.find_parent(0,nums,parent)
    #     print(parent,nums)

    # def find_parent(self,n,arr,parent):
    #     if parent[arr[n]]==-1:
    #         parent[n]=1+self.find_parent(arr[n],arr,parent)
    #         return parent[n]
    #     return parent[arr[n]]+1
        
        
            
            
        
        
        
        
        
    
sol=Solution()
nums = [5,4,0,3,1,6,2]
print(sol.arrayNesting(nums))
    
                