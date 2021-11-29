from typing import List

class Union:
    def __init__(self,n:int) -> None:
        self.parent=[range(n)]
        self.rank=[1]*n
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts=[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
sol=Solution()
print(sol.accountsMerge(accounts))
