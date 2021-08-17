from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_=collections.defaultdict(list)
        for i in range(len(strs)):
            print(strs[i],type(strs[i]))
            x="".join(sorted(strs[i]))
            if x not in hash_:
                hash_[x]=[]
            hash_[x].append(strs[i])
        return list(hash_.values())
    
sol=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
print(sol.groupAnagrams(strs))
x="asmire"
print(sorted(x))