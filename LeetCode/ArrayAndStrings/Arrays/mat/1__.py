from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        i=0
        if len(moves)<=4:return "Pending"
        mat=[[""]*3 for _ in range(3)]
        A=True
        while i<len(moves):
            x=moves[i]
            if A:
                print(x,"X")
                mat[x[0]][x[1]]="A"
                A=False
            else:
                print(x,"O")
                mat[x[0]][x[1]]="B"
                A=True
            i+=1
        # print(mat)         
        for i in range(3):
            if mat[i][0]==mat[i][1]==mat[i][2]=="A" or mat[i][0]==mat[i][1]==mat[i][2]=="B":
                return mat[i][0]
            if mat[0][i]==mat[1][i]==mat[2][i]=="A" or mat[0][i]==mat[1][i]==mat[2][i]=="B":
                return mat[i][0]
        for i in [0,2]:
            if (mat[i][2-i]==mat[1][1]==mat[2-i][i]=="A" or mat[i][2-i]==mat[1][1]==mat[2-i][i]=="B" or
                mat[i][i]==mat[1][1]==mat[2-i][2-i]=="A" or mat[i][i]==mat[1][1]==mat[2-i][2-i]=="B"):
                return mat[1][1]
                 
        if len(moves)==9:
            return "Draw"
        return "Pending"

sol=Solution()
moves=[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# moves=[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# moves = [[0,0],[1,1]]
# moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# moves= [[0,2],[2,0],[2,1],[0,1],[1,2]]
print(sol.tictactoe(moves))
        