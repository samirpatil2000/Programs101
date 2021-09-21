
import math
def countConnectedComp(graph,src,compo_count,visited):
    visited.add(src)
    compo_count[0]+=1
    for e in graph[src]:
        if e not in visited:
            countConnectedComp(graph,e,compo_count,visited)      
    
def connectedSum(graph_nodes,graph_from,graph_to):
    graph={}
    for i in range(1,graph_nodes+1):
        graph[i]=[]
    for i in range(len(graph_from)):
        u,v=graph_from[i],graph_to[i]
        graph[u].append(v)
        graph[v].append(u)
    
    visited=set()
    result=0
    for src in range(1,graph_nodes+1):
        compo_count=[0]
        if src not in visited:
            countConnectedComp(graph,src,compo_count,visited)
            result+=math.ceil(math.sqrt(compo_count[0]))
    return result

graph_nodes=10
graph_from=[1,1,2,3,7]
graph_to=[2,3,4,5,8]
graph_nodes=4
graph_from=[1,1]
graph_to=[2,4]
print(connectedSum(graph_nodes,graph_from,graph_to))