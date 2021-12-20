class Solution:
    def numTilings(self, n: int) -> int:
        if n==0:return 1
        if n in (1,2):
            return n
        if n==3:return 5
        return self.numTilings(n-2)+self.numTilings(n-1)+self.numTilings(n-3)*2
        
    # def dfs_II(self,n:int,memo_1={})->int:
    #     print(n)
    #     # if n in memo_1:return memo_1[n]
    #     if n<=2:
    #         return 0
    #     if n==0:return 1
    #     if n==3:
    #         return 2
    #     memo_1[n]=2+self.dfs_II(n-3)
    #     return memo_1[n]
    # def dfs_I(self, n: int,memo={}) -> int:
    #     if n in memo:return memo[n]
    #     if n in (1,2):
    #         return n
    #     if n==0:return 1
        
    #     memo[n]=self.dfs_I(n-1)+self.dfs_I(n-2)
    #     return memo[n]

        
sol=Solution()
n=4
print(sol.numTilings(n))