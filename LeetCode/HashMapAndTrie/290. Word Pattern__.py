

class Solution:
    def wordPattern(self, t: str, s: str) -> bool:
        s = s.split(' ')
        return len(s) == len(t) and list(map(t.find, t)) == list(map(s.index,s))       
        
        
sol = Solution()
t = "abba"
s = "dog dog dog dog"

print(sol.wordPattern(t,s))