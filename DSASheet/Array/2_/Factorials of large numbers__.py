class Solution:
    def mul(self, num1, num2):
        result = []
        
    def factorial(self, N):
        #code here
        result = [1]
        i = 2
        while i <= N:
            result.append(result[-1] * i)
            i += 1
        return result 

sol = Solution()
print(sol.factorial(10))