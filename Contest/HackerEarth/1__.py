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


class Solution:
    def totalTime(self):
        min_=2**32
        def dfs(src,visited=set(),osf=0):
            if src==N:
                min_=min(min_,osf)
                return
            print(src,visited)
            for e in graph[src]:
                if e in visited:
                    continue
                visited.add(e)
                dfs(src,visited,osf+1+C)
        return dfs(0) 


"""
5 5 3 5
1 2
1 3
2 4
1 4
2 5
"""
sol=Solution()
print(sol.totalTime())


