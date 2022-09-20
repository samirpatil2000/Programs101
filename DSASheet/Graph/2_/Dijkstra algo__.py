import heapq
class Solution:
    def shortest_path(self, graph, src):
        result = []
        queue = [[0, src]]
        heapq.heapify(queue)
        distances = {vertex: float("infinity") for vertex in graph.keys()}
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            result.append([current_vertex, current_distance])
            for edge, distance in graph[current_vertex].items():
                if distances[edge] > current_distance + distance:
                    distances[edge] = current_distance + distance
                    heapq.heappush(queue, [distances[edge], edge])            
        return result
    
    def dijkstra(self, V, graph, src):
        #code here
        queue = [[0, src]]
        heapq.heapify(queue)
        distances = {vertex: float("infinity") for vertex in range(V)}
        distances[src] = 0
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for edge, distance in graph[current_vertex]:
                if distances[edge] > current_distance + distance:
                    distances[edge] = current_distance + distance
                    heapq.heappush(queue, [distances[edge], edge])         
        return distances.values()
    


graph = [
            [[3, 9], [5, 4]], # 0
            [[4, 4]],         # 1
            [[5, 10]],        # 2
            [[0, 9]],         # 3
            [[1, 4], [5, 3]], # 4
            [[0, 4], [2, 10], [4, 3]] # 5
        ]
src = 1
V = 6 
print(Solution().dijkstra(V, graph, src))



    
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}


sol = Solution()
# print(sol.shortest_path(example_graph, src="X"))
V = 2
src = 0
graph = [[[1, 9]] , [[0, 9]]] 
graph = [
            [[3, 9], [5, 4]], # 0
            [[4, 4]],         # 1
            [[5, 10]],        # 2
            [[0, 9]],         # 3
            [[1, 4], [5, 3]], # 4
            [[0, 4], [2, 10], [4, 3]] # 5
        ]
src = 1
V = 6 
print(sol.dijkstra(V, graph, src))

# 6 5
# 0 3 9
# 0 5 4
# 1 4 4
# 2 5 10
# 4 5 3


# v, e = [int(i) for i in input().split(' ')]
# graph = [[] for _ in range(v)]
# for _ in range(e):
#     u, v, w = [int(i) for i in input().split(' ')]
#     graph[u].append([v, w])
#     graph[v].append([u, w])
# print(graph)
    
    
# N,M,T,C=[int(i) for i in n.split(' ')]
# graph=collections.defaultdict(list)
# while M:
#     M-=1
#     n=input()
#     u,v=[int(i) for i in n.split(' ')]
#     graph[u].append(v)
#     graph[v].append(u)


def boggleBoard(board, words):
    # Write your code here.
    visited = [[0] * len(board[0]) for i in range(len(board))]
    matchedWord = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            for word in words:
                if word not in matchedWord:
                    isWordMatched = identifyDirectionToMove(board, word, i, j, 0, visited)
                    print(word, isWordMatched)
                    if isWordMatched:
                        matchedWord.add(word)
    return matchedWord

def identifyDirectionToMove(board, word, i, j, index, visited):
    # print(word, i, j, index, visited)
    if index == len(word):
        return True
    
    if board[i][j] != word[index]:
        return False

    if board[i][j] == word[index] and index == len(word) -1:
        return True
        
    moveRow = [1, 1, 1, 0,-1, -1, -1, 0]
    moveCol = [1, 0, -1, -1, -1, 0, 1, 1]
    visited[i][j] = 1
    isMatched = False
    
    for k in range(8):
        if not (len(board) > i + moveRow[k] >= 0):
            continue
        if not (len(board[0]) > j + moveCol[k] >= 0):
            continue

        if not visited[i + moveRow[k]][j + moveCol[k]]:
            isWordMatched = identifyDirectionToMove(board, word, i + moveRow[k], j + moveCol[k], index + 1, visited)
            if isWordMatched:
                isMatched = isWordMatched 
                break
    visited[i][j] = False
    return isMatched



def identify_direction_to_move(board, word, i, j, index, visited):
    # print(word, i, j, index, visited)
    if index == len(word):
        return True
    
    if board[i][j] != word[index]:
        return False

    if board[i][j] == word[index] and index == len(word) -1:
        return True
        
    moveRow = [1, 1, 1, 0, -1, -1, -1, 0]
    moveCol = [1, 0, -1, -1, -1, 0, 1, 1]
    visited[i][j] = 1
    
    for k in range(8):
        if not (len(board) > i + moveRow[k] >= 0):
            continue
        if not (len(board[0]) > j + moveCol[k] >= 0):
            continue
        new_row = i + moveRow[k]
        new_col = j + moveCol[k]
        
        if not visited[new_row][new_col]:
            is_word_matched = identify_direction_to_move(board, word, new_row, new_col, index + 1, visited)
            if is_word_matched:
                return True
    visited[i][j] = False
    return False



input = {
  "board":[
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
],
  "words": ["this", "is", "not", "RExAxA", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
}

print(boggleBoard(**input))