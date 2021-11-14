


# words=[set(i) for i in words]
# x=["".join(sorted(i)) for i in x]

# print(x)
# print(words)

y={3,4}
x={5,3,4}
a={2,3,4}
b={2,3}

print(b.issubset(a))
print(b.intersection(a,x,y))
print(b.union(a,x,y))


from collections import defaultdict
from typing import List

class Solution:        
    # def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # word_dict=defaultdict(set)
        # for i in range(26):
        #     ch=chr(i+ord('a'))
        #     for w in range(len(words)):
        #         if ch in words[w]:word_dict[ch].add(w)
        # print(word_dict)
        # result=[]
        # for puz in puzzles:
        #     a=word_dict[puz[0]]
        #     x=a.intersection(*[word_dict[i] for i in puz[1:]])
        #     print(puz,a,x)
        #     result.append(len(x))
            
        # return result
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words = [sorted(set(w)) for w in words]
        puzzles = [(p[0], set(p)) for p in puzzles]
        trees = [Trie() for _ in range(26)]
        for w in words:
            for char in w:
                trees[ord(char) - 97].insert(w)
        return [trees[ord(f) - 97].puzzle_match(p) for f,p in puzzles]

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = 0
        
class Trie(object):
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.end += 1
        
    def puzzle_match(self, puzzle):
        def helper(node):
            res[0] += node.end
            for child in node.children:
                if child in puzzle:
                    helper(node.children[child])
        res = [0]
        helper(self.root)
        return res[0]
sol=Solution()
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(sol.findNumOfValidWords(words,puzzles))
    
                