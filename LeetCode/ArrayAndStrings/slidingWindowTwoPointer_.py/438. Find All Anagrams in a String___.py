from cgitb import reset
from typing import List

        
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        unmatch_count = len(p)
        
        if len(p) > len(s):
            return result
        freq_count = [0]*26
        for i in range(len(p)):
            freq_count[ord(p[i]) - ord('a')] += 1
        
        start, end = 0, 0
        for end in range(0, len(p)):
            idx = ord(s[end]) - ord('a')
            if freq_count[idx] > 0:
                unmatch_count -= 1
            freq_count[idx] -= 1
        if unmatch_count == 0:
            result.append(start)
        end += 1
        while end < len(s):
            start_idx = ord(s[start]) - ord('a')
            if freq_count[start_idx] >= 0:
                unmatch_count += 1
            freq_count[start_idx] += 1
            start += 1
            
            end_idx = ord(s[end]) - ord('a')
            if freq_count[end_idx] > 0:
                unmatch_count -= 1
            freq_count[end_idx] -= 1
            
            if unmatch_count == 0:
                result.append(start)
            end += 1
        return result
                
                    
            
    
sol = Solution()
s, p =  "cbaebabacd", "abc"
s, p =  "ab", "b"
print(sol.findAnagrams(s, p))
                
             
