parent=[0]*1000
rank=[i for i in range(1001)]

def findParent(node):
    if node==parent[node]:
        return node
    parent[node]=findParent(parent[node])
    return parent[node]
def union(u,v):
    u=findParent(u)
    v=findParent(v)
    if rank[u]<rank[v]:
        parent[u]=v
    elif rank[u]>rank[v]:
        parent[v]=u
    else:
        parent[v]=u
        rank[u]+=1
        
    