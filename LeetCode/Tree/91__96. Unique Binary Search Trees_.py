# https://leetcode.com/problems/unique-binary-search-trees/

    
class Solution:
    def numTrees(self, n: int) -> int:
        
        def helper(n):
            if n==0 or n==1:
                return n
            return 2*helper(n-1)
        
        return helper(n)
    
    
sol=Solution()
print(sol.numTrees(3))
    
            
            # helper(n,count+1)
        
        
        
        