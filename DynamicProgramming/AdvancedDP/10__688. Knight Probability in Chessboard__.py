class Solution:
    def isValid(self,row,col,n):
        if row>=n or col>=n or row<0 or col<0:
            return False
        return True
        
    def knightProbability(self, n: int, k: int, start_row: int, start_col: int) -> float:
        curr=[[0]*n for _ in range(n)]
        next_=[[0]*n for _ in range(n)]
        
        next_[start_row][start_col]=1
        
        for i in range(k+1):
            for row in range(n):
                for col in range(n):
                    if curr[row][col]:
                        current_row,current_col=row+2,col-1
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                        
                        current_row,current_col=row+2,col+1
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
                        current_row,current_col=row-2,col+1
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
                        current_row,current_col=row-2,col-1
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
                        current_row,current_col=row-1,col+2
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
                        current_row,current_col=row-1,col-2
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
                        current_row,current_col=row+1,col-2
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                        
                        current_row,current_col=row+1,col+2
                        if self.isValid(current_row,current_col,n):
                            next_[current_row][current_col]+=(curr[row][col]/8.0)
                            
            curr=next_
            next_=[[0]*n for _ in range(n)]
        sum_=0.0
        for i in range(n):
            sum_+=sum(curr[i])
        return sum_
        
sol=Solution()
n = 1
k = 0
row = 0
column = 0
print(sol.knightProbability(n,k,row,column))