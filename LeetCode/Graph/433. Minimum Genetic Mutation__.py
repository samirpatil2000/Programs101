from typing import List,Set


class Solution:
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = self.create_graph(words=bank)
        queue = []
        for i in self.get_neighbours(start_word=startGene, words=set(bank)):
            queue.append([i, 1])
        visited = set()
        while queue:
            current_word, current_step = queue.pop(0)
            if current_word in visited:
                continue
            visited.add(current_word)
            if current_word == endGene:
                return current_step
            if current_word not in graph:
                continue
            for e in graph[current_word]:
                if e in visited:
                    continue
                queue.append([e, current_step + 1])
        return -1
    
    def create_graph(self, words):
        graph = {}
        words_set = set(words)
        for i in range(len(words)):
            graph[words[i]] = self.get_neighbours(words[i], words_set)
        return graph
        
    def get_neighbours(self, start_word: str, words: Set[str]) -> None:
        neighbours = set()
        for i in range(26):
            for j in range(len(start_word)):
                new_word = start_word[:j] + chr(i + 65) + start_word[j + 1:]
                if chr(i + 65) != start_word[j] and new_word in words:
                    neighbours.add(new_word)
        return neighbours



                    
sol = Solution()
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]



startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]

from icecream import ic
ic(sol.minMutation(startGene ,endGene ,bank))







# LIKES_CHOICES = ["sweet", "sour", "salty", "bitter", "Savory",
#                      "Bread", "Butter", "Fats", "Milk", "Coffee",
#                      "mud/chalk", "Eggs", "Spicy food", "Meat",
#                      "Fish", "Onions", "Warm food/drinks", "Cold food/drinks", "Fruits", "Other"]

# ic(LIKES_CHOICES)