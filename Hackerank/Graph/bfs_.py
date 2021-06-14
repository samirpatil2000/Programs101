def bfs(n, m, edges, s):
    # Write your code here
    
    graph={}
    for i in range(n):
        graph[i+1]=[]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited=set()
    result={}
    q=[[s,1]]
    # level=6
    while q:
        temp,level=q.pop(0)
        if temp in visited:continue
        visited.add(temp)
        for edge in graph[temp]:
            if edge not in visited:
                result[edge]=6*level
                q.append([edge,level+1])
    new_result = []
    for node in range(1, n+1):
        if s != node:
            new_result.append(result.get(node, -1))
    return new_result


q = int(input().strip())
for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))
    print(edges)
    s = int(input().strip())

    result = bfs(n, m, edges, s)
    print(result)