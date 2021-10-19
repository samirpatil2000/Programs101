import collections


class TrieNode:
    
    def __init__(self) -> None:
        self.children=collections.defaultdict(TrieNode)
        self.val=0
        
class Trie: 
    def __init__(self) -> None:
        self.root=TrieNode()
    
    def insert(self,key,val):
        curr=self.root
        for w in key:
            curr=curr.children[w]
        curr.val=val
    
    def sum(self,key):
        curr=self.root
        for w in key:
            if w not in curr.children:
                return 0
            curr=curr.children[w]
        return self.dfs(curr)
    
    def dfs(self,node:TrieNode):
        sum_=0
        for w in node.children.values():
            sum_+=self.dfs(w)
        return sum_+node.val
        # return sum([self.dfs(w) for w in node.children.values()])+node.val
        
    
    
obj=Trie()
obj.insert("apple",3)
obj.insert("app",2)
obj.insert("ap",10)
print(obj.sum("app"))
print(obj.sum("a"))
