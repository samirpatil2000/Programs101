from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        min_len = 2 ** 32
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))
        first = strs[0][:min_len]
        for i in range(min_len):
            for str_ in strs[1:]:
                if str_ == "":
                    return ""
                if str_[i] != first[i]:
                    return first[:i]
        return first
    
sol = Solution()
strs = ["flower","flow","flight"]
strs = ["ab", "a"]
print(sol.longestCommonPrefix(strs))