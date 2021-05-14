class Solution:
    def allPathsSourceTarget(self, graph):
        compo_list=[]

        def dfs(src,list_):
            if len(graph[src])==0:
                compo_list.append(list_)
                return                
            for i in graph[src]:
                dfs(i,list_+[i])
        
        dfs(0,[0]) 
        return compo_list
    
    
graph = [[1,2],[3],[3],[]]
sol=Solution()
print(sol.allPathsSourceTarget(graph))