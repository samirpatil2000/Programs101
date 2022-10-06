class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            max_ = -1
            for j in (x, y, z):
                if i >= j:max_ = max(max_, dp[i - j]) 
            dp[i] = max_ + 1 if max_ != -1 else -1
        return 0 if dp[-1] == -1 else dp[-1]

sol = Solution()
n = 4
x = 2
y = 1
z = 1

n = 5
x = 5
y = 3
z = 2

n = 7
7
x, y, z = 5, 5, 2
n =9999
x,y ,z = 94, 20, 244
print(sol.maximizeTheCuts(n, x, y, z))