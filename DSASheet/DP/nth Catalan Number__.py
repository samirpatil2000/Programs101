from math import factorial


class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self, n):
        #return the nth Catalan number.
        catalan = [1] * (n + 1)
        for i in range(2, n + 1):
            result = 0
            for j in range(i):
                result += (catalan[j] * catalan[i - j - 1])
            catalan[i] = result
        return catalan[-1]
n = 100
print(Solution().findCatalan(n))
                
