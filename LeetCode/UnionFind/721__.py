from typing import List
import collections
class Union:
    def __init__(self,n:int) -> None:
        self.parent=list(range(n))
        self.rank=[1]*n
        
    def findParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        u_parent=self.findParent(u)
        v_parent=self.findParent(v)
        if self.rank[u_parent]<self.rank[v_parent]:
            self.parent[u_parent]=v_parent
            self.rank[v_parent]+=self.rank[u_parent]
        else:
            self.parent[v_parent]=u_parent
            self.rank[u_parent]+=self.rank[v_parent]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        uf=Union(n)
        dict_={}
        for i,acc in enumerate(accounts):
            for e in acc[1:]:
                if e in dict_:
                    uf.union(dict_[e],i)
                else:
                    dict_[e]=i
        print(dict_,uf.parent)
        ans=collections.defaultdict(list)
        for email,parent in dict_.items():
            ans[uf.findParent(parent)].append(email)
        return [[accounts[i][0]]+sorted(emails) for i,emails in ans.items()]
    
    
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution2:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        print(ownership,uf.parents)
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts=[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
accounts=[["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
# accounts=[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
sol=Solution()
sol=Solution()
x=sol.accountsMerge(accounts)
sol2=Solution2()
y=sol2.accountsMerge(accounts)
if x==y:
    print(True)
else:
    print(False)