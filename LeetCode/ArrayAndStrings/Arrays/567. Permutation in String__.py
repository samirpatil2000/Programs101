class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        unmatch_count = len(s1)
        
        if len(s1) > len(s2):
            return False
        freq = [0]*26
        for i in s1:
            freq[ord(i) - ord('a')] += 1
        
        start, end = 0, 0
        for end in range(0, len(s1)):
            idx = ord(s1[end]) - ord('a')
            if freq[idx] > 0:
                unmatch_count -= 1
            freq[idx] -= 1
        if unmatch_count == 0:
            return True
        end += 1
        while end < len(s2):
            start_idx = ord(s2[start]) - ord('a')
            if freq[start_idx] >= 0:
                unmatch_count += 1
            freq[start_idx] += 1
            start += 1
            
            end_idx = ord(s2[end]) - ord('a')
            if freq[end_idx] > 0:
                unmatch_count -= 1
            freq[end_idx] -= 1
            if unmatch_count == 0:
                return True
            end += 1
        return False
            
            
        