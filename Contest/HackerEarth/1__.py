'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import collections
n=input()
N,M,T,C=[int(i) for i in n.split(' ')]
graph=collections.defaultdict(list)
while M:
    M-=1
    n=input()
    u,v=[int(i) for i in n.split(' ')]
    graph[u].append(v)
    graph[v].append(u)


def dfs(src,visited=set()):
    if src in visited:return 2**32
    visited.add(src)
    if src==N:
        return C
    print(src,visited)
    min_=0
    for e in graph[src]:
        min_=min(min_,dfs(e,visited))
    
    if not min_:
        return 2**32   
    return min_+1+C

print(dfs(1))






