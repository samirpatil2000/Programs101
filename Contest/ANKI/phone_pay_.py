class Solution:
    def findRelics(self, s:str):
        result = 0
        set_ = set()
        for i in range(len(s)):
            if s[i] in set_:
                set_.clear()                
            set_.add(s[i])
            result = max(len(set_), result)
        return result

sol = Solution()
s = "gkPPkgk"
print(sol.findRelics(s))