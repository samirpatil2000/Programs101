import collections
from typing import List
class Trie:
    def __init__(self) -> None:
        self.root=collections.defaultdict(dict)
    
    def insert(self,word:str):
        curr=self.root
        for w in word[::-1]:
            if w not in curr:
                curr[w]={} 
            curr=curr[w]
        curr["end"]=True
        
    def search(self,word):
        curr=self.root
        for w in word:
            if "end" in curr:
                return True
            if w not in curr:
                return False
            else:
                curr=curr[w]
        return "end" in curr
    

class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.trie=Trie()
        self.prev_str=""
        for word in words:
            print(word[::-1])
            self.trie.insert(word)
            
        

    def query(self, letter: str) -> bool:
        
        self.prev_str=letter+self.prev_str
        print(self.trie.root,self.prev_str)
        return self.trie.search(self.prev_str)


# Your StreamChecker object will be instantiated and called as such:
x=[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
obj = StreamChecker(words=x[0][0])
for i in x[1:]:
    param_1 = obj.query(i[0])
    print(param_1,i)