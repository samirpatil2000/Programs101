
class Solution:
    def countFriendsPairings(self, n):
        # code here 
        if n in (0, 1):
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        mod = (10 ** 9 )+ 7
        print(mod)
        print(10e9 + 7)
        
        
        for i in range(3, n + 1):
            
            dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % mod
        return int(dp[-1])
    def countFriendsPairings_2(self, n):
        dp_1 = 1
        dp_2 = 2
        mod = 10e9 + 7
        
        for i in range(3, n + 1):
            temp = dp_1
            dp_1 = dp_2
            dp_2 = (dp_2 + (i - 1) * temp) % mod
        return dp_2
    
sol = Solution()
n = 5
print(sol.countFriendsPairings(n))
print(sol.countFriendsPairings_2(n))

