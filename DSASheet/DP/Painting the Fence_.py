
class Solution:
    
    def countWays(self, n, k):
        mod = 10e8
        mod += 7
        same = k * 1
        diff = k * (k - 1)
        total = same + diff
        for i in range(3, n + 1):
            same = diff * 1
            diff = total * (k - 1)
            total = (same + diff) % mod
            print(total)
        return int(total)

    
sol = Solution()
n = 3
k = 2
n = 1
k = 17
print(sol.countWays(n, k))
             
            