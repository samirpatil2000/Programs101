from collections import defaultdict, deque
class Solution:
    largest_cycle_length = 0
    max_cycle_len_sum = 0
    def create_graph(self, edges):
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
        return graph
    
    def find_max_weight_node(self, edges):
        max_weight = -1
        max_node = -1
        weights = [0] * len(edges)

        for i in range(len(edges)):
            if edges[i] != -1:
                weights[edges[i]] += 1
        
        for i in range(len(edges)):
            if weights[i] > max_weight:
                max_weight = weights[i]
                max_node = i
        return max_node

    def dfs(self, graph, node, start_node, cycle_length, cycle_sum, visited):
        visited[node] = True
        for edge in graph[node]:
            if edge == start_node:
                if self.largest_cycle_length < cycle_length + 1:
                    self.largest_cycle_length = cycle_length + 1
                    self.max_cycle_len_sum = cycle_sum
            elif not visited[edge]:
                self.dfs(graph, edge, start_node, cycle_length + 1, cycle_sum + edge, visited)

        visited[node] = False
    
    def find_largest_cycle_length(self, edges):
        graph = self.create_graph(edges)
        visited = [False] * len(edges)

        for i in range(len(edges)):
            self.dfs(graph, i, i, 0, i, visited)

        if self.largest_cycle_length == 0:
            return -1
        return self.max_cycle_len_sum
    
    
    def nearest_meeting_cell(self, x1, x2, edges):
        visited1 = set()    
        visited2 = set()
        queue1 = deque([x1])    
        queue2 = deque([x2])    
        steps1, steps2 = 0, 0
        graph = self.create_graph(edges)
        while queue1 or queue2:
            for _ in range(len(queue1)):
                node = queue1.popleft()
                if node in visited2:
                    return node    # found nearest meeting cell
                visited1.add(node)
                for edge in graph[node]:
                    if edge not in visited1:
                        queue1.append(edge)
            steps1 += 1
            
            for _ in range(len(queue2)):
                node = queue2.popleft()
                if node in visited1:
                    return node  
                visited2.add(node)
                for edge in graph[node]:
                    if edge not in visited2:
                        queue2.append(edge)
                        
            steps2 += 1
            
        return -1    # no meeting cell found
    

# t = int(input())
# while t:
#     t -= 1
#     edges = [int(i) for i in input().strip().split()]
#     print(Solution().find_max_weight_node(edges))
    
edges = [1, 2, 3, 4, 0]
edges = [1, 2, -1, 4, 5, -1, -1]
edges =  [1, 2, 3, -1, 5, 6, 0, 7, 8]
# edges = [1, 0, 3, -1, 5, 4]
print(Solution().find_largest_cycle_length(edges))
print(Solution().find_max_weight_node(edges))
            
edges = [2, 2, 5, 4, 8, 3, 2, 6, 6]
x1, x2 = 0,8
# print(Solution().nearest_meeting_cell(x1, x2, edges))

url = "https://www.google.com/search"
url = "https://www.google.com:455/search.html/to/path"
# url = "http://localhost:9043"
    
def get_port(hostname):
    if len(hostname.split(":")) > 1:
        return hostname.split(":")[-1]
    return "443"

def is_secure(s):
    if "https:" == s:
        return "Y"
    return "N"
    
def parseUrl(url: str):
    parsed_url = url.split("/")
    print(parsed_url)
    file = ""
    if len(parsed_url) > 3:
        if len(parsed_url) > 3:
            file = "/".join(parsed_url[3:])
    print("GET /" + file + " HTTP/2")
    
    print("Host: " + parsed_url[2].split(":")[0])
    print("X-Port: " + get_port(parsed_url[2]))
    print("X-Secure-Protocol: " + is_secure(parsed_url[0]))
    
parseUrl(url)