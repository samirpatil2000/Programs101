class Solution:
    def numTrees(self, n: int) -> int:
        def dfs(left:int,right:int,memo={}):
            x=str(left)+"-"+str(right)
            if x in memo:return memo[x]
            if left>=right:return 1
            result=0
            for i in range(left,right+1):
                result+=(dfs(left,i-1,memo)*dfs(i+1,right,memo))
            memo[x]=result
            return result
        return dfs(1,n)
    
sol=Solution()
n=19
print(sol.numTrees(n))