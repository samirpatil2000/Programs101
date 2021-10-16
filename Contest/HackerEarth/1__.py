'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import collections
from typing import List

def inputFun():
    n=input()
    N,M,T,C=[int(i) for i in n.split(' ')]
    graph=collections.defaultdict(list)
    while M:
        M-=1
        n=input()
        u,v=[int(i) for i in n.split(' ')]
        graph[u].append(v)
        graph[v].append(u)

›

class Solution:
    def totalTime(self,graph:collections.defaultdict(List),N:int,C:int,T:int):
        visited=set()
        
        def dfs(src):
            print(src)
            if src in visited:
                return (False,-1)
            if src==N:
                return (True,C)
            visited.add(src)
            
            for e in graph[src]:
                if e not in visited:
                    x=dfs(e)
                    if x[0]:
                        return (True,x[1]+T+C)
            return (False,-1)
        
        return dfs(1)
                



sol=Solution()

N,M,C,T=5,5,3,5
print(sol.totalTime(graph,N,C,T))


