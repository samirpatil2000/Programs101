from typing import List


class Solution:
    def partions(self,n,k):
        
        
        def dfs(index,subsets:List[List[int]]):
            if index==n+1:
                print(subsets)
                return
            for subset in subsets:
                if len(subset)>0:
                    subset.append(index)
                    dfs(index+1,subsets)
                    subset.pop()
                else:
                    subset.append(index)
                    dfs(index+1,subsets)
                    subset.pop()
                    break
            
        
        subsets=[[] for _ in range(k)]
        print(subsets)
        dfs(1,subsets)    
        
        
sol=Solution()
n,k=3,2
print(sol.partions(n,k))
        

