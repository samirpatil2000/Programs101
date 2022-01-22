class Solution:
    def winnerSquareGame(self, n: int, memo = {}) -> bool:

        if n in memo:
            return memo[n]
        aliceWins = False
        step = 1
        while step * step <= n:
            if n - step * step == 0:
                aliceWins = True
                break
            else:
                aliceWins = aliceWins or not self.winnerSquareGame(n - step * step, memo)
            step += 1
        memo[n] = aliceWins
        return aliceWins
    
sol = Solution()
n = 7
print(sol.winnerSquareGame(n))