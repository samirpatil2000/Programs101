# class Solution():


def topoSort(graph,src,visited,st):
    visited.add(src)
    for edge in graph[src]:
        if edge not in visited:
            topoSort(graph,edge,visited,st)
    st.append(src)
    
def findOrder(words,N):
    graph=dict()
    for i in range(N):
        graph[chr(i+97)]=[]
    for i in range(len(words)-1):
        j=0
        while j<min(len(words[i]),len(words[i+1])) and words[i][j]==words[i+1][j]:
            j+=1
        print(words[i][j],words[i+1][j],words[i],words[i+1])
        graph[words[i+1][j]].append(words[i][j])
    visited=set()
    st=[]
    print(graph)
    for i in graph.keys():
        if i not in visited:
            topoSort(graph,i,visited,st)
    return st

words=["baa","abcd","abca","cab","cad"]  
N=4
print(findOrder(words,N))  