from typing import List


class Solution:
    
    def exist_2(self, board: List[List[str]], word: str) -> bool:
        if not board:return False
        if not word:return False
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(row,col,word):
            if len(word)==0:
                return True
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
                return False
            if board[row][col]=="#":return False
            if board[row][col]!=word[0]:return False
    
            temp=board[row][col]
            board[row][col]="#"
            for i,j in d:
                new_row,new_col=row+i,col+j
                if dfs(new_row,new_col,word[1:]):
                    return True
            board[row][col]=temp
            return False
        for  i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,word):
                    return True
        return False
    
    def exist(self, board, word):
        '''return true if word is empty'''
        if not word: return True
        if not board:return False
        m, n, w = len(board), len(board[0]), len(word) - 1 
        def dfs(i, j, k):         
            if i < 0 or i >= m or j < 0 or j >= n:
                return False        
            if board[i][j] == '#':
                return False  
            if board[i][j] != word[k]:
                return False       
            if k == w:return True
            tmp = board[i][j] 
            board[i][j] = '#'
            k += 1
            for x, y in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                if dfs(i + x, j + y, k):
                    return True
            board[i][j] = tmp
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
    
    
sol=Solution()
board=[["a","a"]]
word="aa"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
# print(sol.exist(board,word))
print(sol.exist_2(board,word))