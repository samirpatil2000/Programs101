from typing import List


class Solution:
    def isValid(self,board,row,col,num):
        for curr_col in range(len(board)):
            if board[row][curr_col] == num:
                return False
        for curr_row in range(len(board)):
            if board[curr_row][col] == num:
                return False
        sub_matrix_row = (row // 3)*3
        sub_matrix_col=(col // 3)*3
        for i in range(0,3):
            for j in range(0,3):
                if board[sub_matrix_row+i][sub_matrix_col+j]==num:
                    return False
        return True
    
    def solve(self,board,row,col):
        if row == len(board):
            print(board)
            return
        new_row=new_col=0
        if col==len(board)-1:
            new_row=row+1
            new_col=0
        else:
            new_row=row
            new_col=col+1
        if board[row][col]!=".":
            self.solve(board,new_row,new_col)
        else:
            for pos in range(1,10):
                if self.isValid(board,row,col,str(pos)):
                    board[row][col]=str(pos)
                    self.solve(board,new_row,new_col)
                    board[row][col]="."
            
    def solveSudoku(self, board: List[List[str]],row=0,col=0) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.solve(board,0,0)
        if row == len(board):
            return True
        new_row=new_col=0
        if col==len(board)-1:
            new_row=row+1
            new_col=0
        else:
            new_row=row
            new_col=col+1
        if board[row][col]!=".":
            if self.solveSudoku(board,new_row,new_col)==True:
                return True
        else:
            for pos in range(1,10):
                if self.isValid(board,row,col,str(pos)):
                    board[row][col]=str(pos)
                    if self.solveSudoku(board,new_row,new_col)==True:
                        return True
                    board[row][col]="."
            return False
        
sol=Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sol.solveSudoku(board))
print(board)
        
        
        