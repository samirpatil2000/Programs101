import collections
class TrieNode:  
    def __init__(self) -> None:
        self.children=collections.defaultdict(TrieNode)
        self.isEnd=False
        
    def insert(self,word):
        if not word:
            self.isEnd=True
        else: 
            self.children[word[0]].insert(word[1:])
    
    def search(self,word):
        if not word:
            return self.isEnd
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False
    
    def startsWith(self,prefix):
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].search(prefix[1:])
        return False
    
        



class Trienode:
    def __init__(self) -> None:
        self.root={}
    
    def insert(self,word):
        curr=self.root
        for w in word:
            if w not in curr:
                curr[w]={}    
            curr=curr[w]
        curr["end"]=True
        
    def search(self,word):
        curr=self.root
        for w in word:
            if w not in curr:
                return False
            else:
                curr=curr[w]
        return "end" in curr
    
    def startsWith(self,prefix):
        curr=self.root
        for w in prefix:
            if w not in curr:
                return False
            else:
                curr=curr[w]
        return True
    
# obj=TrieNode()
# obj.insert("apple")
# obj.insert("app")
# obj.insert("beer")
# print(obj.search("appl"))
# print(obj.children)


    
obj=Trienode()
obj.insert("apple")
obj.insert("app")
obj.insert("appil")
obj.insert("beer")
print(obj.search("appl"))
print(obj.root)