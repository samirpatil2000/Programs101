from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count_=0
        words=set(words)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(s[i:j])
                if s[i:j] in words:
                    count_+=1
        return count_
    
    
sol=Solution()
s = "abcde"
words = ["a","bb","acd","ace"]
print(sol.numMatchingSubseq(s,words))