class Graph:
     
    def findParent(self,node,parent):
        if node==parent[node]:
            return node
        parent[node]=self.findParent(parent[node],parent)
        return parent[node]
    
    def mainAlgo(self,c_to,c_from,edges,nodes):
        parent=[i for i in range(nodes+1)]
        max_array=[i for i in range(nodes+1)]
        print(max_array)
        total_sum=sum(max_array)
        result=[]
        for i in range(edges):
            u=self.findParent(c_to[i],parent)
            v=self.findParent(c_from[i],parent)
            parent[v]=u
            max_array[c_to[i]]=max(max_array[c_to[i]],c_from[i])
            max_array[c_from[i]]=0
            # print(max_array,c_from[i],c_to[i])
            result.append(sum(max_array))
        return result,parent
    

sol=Graph()
c_from=[1,2,1,4]
c_to=[2,3,3,5]
edges=4
nodes=5
print(sol.mainAlgo(c_to,c_from,edges,nodes))
        
            
        