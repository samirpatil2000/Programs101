class Solution:
    
    def dfs(self, str1: str, str2: str, i: int, j: int, memo={}) -> int:
        if i == len(str1) and j == len(str2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(str1):
            return len(str2) - j
        if j == len(str2):
            return len(str1) - i
        if str1[i] == str2[j]:
            result = self.dfs(str1, str2, i + 1, j + 1, memo)
        else:
            result = min(
                self.dfs(str1, str2, i + 1, j + 1, memo),
                self.dfs(str1, str2, i, j + 1, memo),
                self.dfs(str1, str2, i + 1, j, memo)
                    ) +  1
        memo[(i, j)] = result
        
        return result
        
    def edit_distance(self, str1: str, str2: str):
        memo = {}
        return self.dfs(str1, str2, 0, 0, memo)
    def minDistance(self, word1, word2, i=0, j=0, memo={}):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance(word1, word2, i + 1, j + 1, memo)
            else: 
                insert = 1 + self.minDistance(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]

s1, s2 = "intention", "execution"
# print(Solution().edit_distance(s1, s2))
print(Solution().minDistance(s1, s2))