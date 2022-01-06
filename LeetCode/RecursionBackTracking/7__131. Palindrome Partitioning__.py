from typing import List


class Solution:
    def partition(self, s: str,start=0) -> List[List[str]]:
        if start==len(s):
            return [[]]
        result=[]
        for i in range(start,len(s)):
            curr=s[start:i+1]
            print(curr)
            if curr==curr[::-1]:
                result+=[[curr]+rem for rem in self.partition(s,i+1)]
        return result
                
            
            

sol=Solution()
s="efe"
print(sol.partition(s))
