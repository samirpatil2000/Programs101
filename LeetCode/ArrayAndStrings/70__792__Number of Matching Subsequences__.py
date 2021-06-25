from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count_=0
        map_={}
        for i in range(len(s)):
            if s[i] not in map_:
                map_[s[i]]=[]
        for i in range(len(words)):
            if words[i][0] in map_:
                map_[words[i][0]].append(words[i])
        for i in range(len(s)):
            for _ in range(len(map_[s[i]])):
                x=map_[s[i]][0][1:]
                map_[s[i]].pop(0)
                if len(x)==0:
                    count_+=1
                else:
                    if x[0] in map_:
                        map_[x[0]].append(x)
        return count_
    
    
                    
                    
                
                    
    
sol=Solution()
s = "abcde"
words = ["a","bb","acd","ace"]

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
print(sol.numMatchingSubseq(s,words))

# print(s[:])