from typing import List


class Solution:
    
    def printAllMinCostPaths(self, mat:List[List[int]]):
        dp=mat.copy()
        n=len(mat)
        m=len(mat[0])
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if row==n-1 and col==m-1:
                    dp[row][col]=mat[row][col]
                elif row==n-1:
                    dp[row][col]=mat[row][col]+dp[row][col+1]
                elif col==m-1:
                    dp[row][col]=mat[row][col]+dp[row+1][col]
                else:
                    dp[row][col]=mat[row][col]+min(dp[row+1][col],dp[row][col+1])
        q=[[0,0,str(dp[0][0])]]    
        while q:
            row,col,res=q.pop(0)
            
            if row==n-1 and col==m-1:
                print(res)
            if row==n-1:
                q.append([row,col+1,res+"-"+str(dp[row][col+1])])
            elif col==n-1:
                q.append([row+1,col,res+"-"+str(dp[row+1][col])])
            elif row<=n-1 and col<=m-1:
                if dp[row+1][col] < dp[row][col+1]:
                    q.append([row+1,col,res+"-"+str(dp[row+1][col])])
                elif dp[row+1][col] > dp[row][col+1]:
                    q.append([row,col+1,res+"-"+str(dp[row][col+1])])
                else:
                    q.append([row+1,col,res+"-"+str(dp[row+1][col])])
                    q.append([row,col+1,res+"-"+str(dp[row][col+1])])
                    
        
sol=Solution()
sol.printAllMinCostPaths(mat=[[1,2,3],[4,5,6],[7,8,9]])
        