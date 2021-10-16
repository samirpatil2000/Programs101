from typing import List


class Solution:
    def wordIntialIndex(self,board:List[List[str]], words: List[str],n:int,m:int):
        
        hash_={word[0]:[] for word in words}
        for row in range(n):
            for col in range(m):
                if board[row][col] in hash_:
                    hash_[board[row][col]].append((row,col))
        return hash_
        
    
    def dfs(self,board:List[List[str]],word,row,col,index):
        n=len(board)
        m=len(board[0])
        
        if row<0 or col<0 or row>=n or col>=m:
            return False
        
        if board[row][col]=="#" or word[index]!=board[row][col]:
            return False
        if index==len(word)-1:
            print(index,row,col,word[index])
            return True
        temp=board[row][col]
        board[row][col]="#"
        
        for r,c in ((1,0),(-1,0),(0,1),(0,-1)):
            if self.dfs(board,word,row+r,col+c,index+1):
                board[row][col]=temp
                return True
        board[row][col]=temp
        return False
                
        
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n=len(board)
        m=len(board[0])
        # if n==1 and m==1:
        #     return [words[0]] if words[0]==board[0][0] else []
        hash_=self.wordIntialIndex(board,words,n,m)
        
        
        
        def dfs(board,word,i, j, k):         
            if i < 0 or i >= m or j < 0 or j >= n:
                return False        
            if board[i][j] == '#':
                return False  
            if board[i][j] != word[k]:
                return False       
            if k == len(word)-1:return True
            
            k += 1
            
            tmp = board[i][j] 
            board[i][j] = '#'
            for x, y in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                if dfs(board,word,i + x, j + y, k):
                    board[i][j] = tmp
                    return True
            board[i][j] = tmp
            return False
        
        result=[]
        print(hash_)
        for word in words:
            for row,col in hash_.get(word[0],[]):
                print(word,row,col)
                if self.dfs(board,word,row,col,0):
                    print(row,col)
                    result.append(word)
                    break
        return result
                
                
                
        
sol=Solution()
board,words=[["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]
board,words=[["a","a"]],["aaa"]
board,words=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]
board,words=[["a"]],["b","a"]
print(sol.findWords(board,words))