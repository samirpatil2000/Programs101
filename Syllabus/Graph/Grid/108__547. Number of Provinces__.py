class Solution(object):
    
    
    def findCircleNumUsingDFS(self, mat):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited=set()
        def dfs(src):
            visited.add(src)
            for i,edge in enumerate(mat[src]):
                if edge==1 and i not in visited:
                    dfs(i)
                
        cnt=0   
        for i in range(len(mat)):
            if i not in visited:
                dfs(i)
                cnt+=1
        return cnt
            
            
    
    
    
sol=Solution()
              # 0 1 2
isConnected = [[1,1,0], # 0
               [1,1,0], # 1
               [0,0,1]] # 2
print(sol.findCircleNumUsingDFS(isConnected))