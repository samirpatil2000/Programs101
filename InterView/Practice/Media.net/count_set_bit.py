
class Solution:
    
    def count_set_bit(self, n: int):
        if n < 1:
            return 0
        result = 1
        num = 2
        while num <= n:
            result += 1
            num *= 2
        return result
    

print(Solution().count_set_bit(2))