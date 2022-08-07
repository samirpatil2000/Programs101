#User function Template for python3
result = []
class Solution:
    
    def find_permutation(self, S:str, out = ""):
        # Code here
        if len(S) == 0:
            result.append(out)
            return
        for i in range(len(S)):
            if i > 0 and S[i] == S[i - 1]:
                continue
            self.find_permutation(S[:i] + S[i + 1:], out + S[i])
        return
    
    def find_permutation_bottom_up(self, S:str, out = ""):
        # Code here
        if len(S) == 0:
            print(out, end = " ")
            return []
        for i in range(len(S)):
            if i > 0 and S[i] == S[i - 1]:
                continue
            self.find_permutation_bottom_up(S[:i] + S[i + 1:], out + S[i])
        return

sol = Solution()
s = "ljr"
s = list(s)
s.sort()
print(sol.find_permutation(s))
result.sort()
print(result)
"jlr jrl ljr lrj rjl rlj"