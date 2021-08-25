from typing import List
from functools import reduce

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for i in range(len(words)):
            print(list(allowed)+list(words[i]))
            ans=0
            for j in list(allowed)+list(words[i]):
                ans^=ord(j)
            print(ans)
            # x=reduce(lambda x,y:ord(x)^ord(y) ,list(allowed)+list(words[i]))
            # print(x)
            
sol=Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
sol.countConsistentStrings(allowed,words)
            
                