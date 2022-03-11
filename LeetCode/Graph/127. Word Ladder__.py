from collections import deque
from termios import VDISCARD
from unittest import result
class Solution:
    
    def get_edges(self, word):
        result_set = set()
        for a in range(26):
            for i in range(len(word)):
                tar_word = word[:i] + chr(a + 97) + word[i+1:]
                if word != tar_word and tar_word in wordList:
                    result_set.add(tar_word)
        return result_set
                    
    def create_graph(self, wordList):
        graph = {}
        for word in wordList:
            graph[word] = self.get_edges(word)
        return graph
                
    def ladderLength(self, beginWord, endWord, wordList):
        graph = self.create_graph(set(wordList))
        queue = deque()
        print(graph)
        for e in self.get_edges(beginWord):
            queue.append([e, 1])
        visited = set()
        print(queue)
        while(queue):
            node, height = queue.popleft()
            print(node, height)
            if node == endWord:
                return height + 1
            if node in visited:
                continue
            visited.add(node)
            for src in graph[node]:
                queue.append([src, height + 1])
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# wordList = ["hot","dot","dog","lot","log"]

beginWord, endWord, wordList = "red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))

print(chr(98))