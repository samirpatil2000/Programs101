from collections import defaultdict
from logging import root


class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.isWord =False
class WordDictionary:
    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word + '$':
            if ch not in node:
                node[ch] = dict()

            node = node[ch]

    def search(self, word: str) -> bool:
        nodes = [self.trie]
        for ch in word + '$':
            new_nodes = []
            for node in nodes:
                if ch == '.': 
                    new_nodes += [v for v in node.values()]
                elif ch in node: 
                    new_nodes.append(node[ch])

            if not new_nodes:
                return False

            nodes = new_nodes
            
        return True
    
    # def __init__(self):
    #     self.root = Trie()

    # def addWord(self, word: str) -> None:
    #     root = self.root
    #     for w in word:
    #         if w not in root.children:
    #             root.children[w] = Trie()
    #         root = root.children[w]
    #     root.isWord = True
                
    # def search(self, word: str) -> bool:
    #     nodes = [self.root]
    #     for w in word+"$":
    #         new_nodes = []
    #         for node in nodes:
    #             if w == ".":
    #                 new_nodes += [v for v in node.children]
    #             if w in node.children:
    #                 new_nodes.append(node)
    #         if not new_nodes:
    #             return False
    #         nodes = new_nodes
    #     return False
    
obj = WordDictionary()
word = ["addWord","addWord","addWord","search","search","search","search"]
_list = [["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
result =[]
for i in range(len(_list)):
    param_2 = "None"
    if word[i] == "addWord":
        obj.addWord(_list[i][0])
    else:    
        param_2 = obj.search(_list[i][0])
        
    result.append(param_2)
    
print(result)