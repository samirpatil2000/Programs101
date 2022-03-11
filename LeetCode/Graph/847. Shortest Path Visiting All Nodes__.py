from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        final_state = (1 << len(graph)) - 1
        queue = deque()
        for i in range(len(graph)):
            queue.append([i, 1 << i])
        print(queue)
        
        visited = set()
        
        shortest_path = 0
        while queue:
            shortest_path += 1
            for i in range(len(queue)):
                head = queue.popleft()
                for e in graph[head[0]]:
                    new_visited_node = head[1] | (1 << e)
                    x = str(e) + "-" + str(new_visited_node)
                    if x in visited:
                        continue
                    visited.add(x)
                    if new_visited_node == final_state:
                        return shortest_path
                    queue.append([e, new_visited_node])
                    
        return -1
    
    
sol = Solution()
graph = [[1,2,3],[0],[0],[0]]
print(sol.shortestPathLength(graph))