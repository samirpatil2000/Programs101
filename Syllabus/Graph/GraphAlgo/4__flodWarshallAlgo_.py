class Solution():
    def flodAlgo(self,mat):
        for k in range(len(mat)):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j]==-1:
                        mat[i][j]=10000000
                    mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])
                    
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]==10000000:
                    mat[i][j]=-1


sol=Solution()
matrix=[[0,1,43],[1,0,6],[-1,-1,0]]
print(sol.flodAlgo(matrix))
print(matrix)      
        
        