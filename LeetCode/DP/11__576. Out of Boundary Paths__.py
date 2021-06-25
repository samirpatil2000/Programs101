class Solution:
    def isValid(self,row,col,m,n):
        if row>=m or col>=n or col<0 or row<0:
            return False
        return True
        
    def findPaths2(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mat=[[0]*n for _ in range(m)]
        memo={}
        dr=[+1,-1,0,0]
        dc=[0,0,+1,-1]
        def dfs(mat,row,col,k):
            str_=str(row)+str(col)+str(k)
            if str_ in memo:return memo[str_]
            if row==m and col==n:
                if k>0:
                    if row==col==1:return 4
                    elif row==1 or col==1:return 3
                    else: return 2
                else:return 0  
            count_=0
            for i in range(4):
                current_row=row+dr[i]
                current_col=col+dc[i]
                if self.isValid(current_row,current_col,m,n):
                    if k>0:
                        count_+=dfs(mat,current_row,current_col,k-1)
                elif k>0:count_+=1
            # print(row,col,k)
            count_=count_%(1000000000+7)
            memo[str_]=count_
            return count_
        return dfs(mat,startRow,startColumn,maxMove)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        def dfs(row,col,k):
            if k<0:return 0
            if row>=m or col>=n or col<0 or row<0:return 1 
            if dp[row][col][k] != -1:
                return dp[row][col][k]
            count_=0
                
            count_ += dfs(row-1, col, k - 1)
            count_ += dfs(row+1, col, k - 1)
            count_ += dfs(row, col-1, k - 1)
            count_ += dfs(row, col+1, k - 1)

            dp[row][col][k]=count_
            return count_
        return dfs(startRow,startColumn,maxMove)%(10**9+7)
        
    
    
sol=Solution()
m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0

m =  36
n =  5
maxMove =  50
startRow = 15
startColumn = 3
print(sol.findPaths(m,n,maxMove,startRow,startColumn))
print(sol.findPaths2(m,n,maxMove,startRow,startColumn))
            
            