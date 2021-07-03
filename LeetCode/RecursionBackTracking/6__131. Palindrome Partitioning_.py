from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        list_=[]
        def dfs(s:str,out_=[]):
            print(out_)
            if not s:
                list_.append(out_)
                return
            for i in range(1,len(s)):
                print(s[:i],s[:i][::-1])
                if s[:i]==s[:i][::-1]:
                    dfs(s[i:],out_+[s[:i]])
        dfs(s)
        return list_
    
sol=Solution()
s="aab"
print(sol.partition(s))