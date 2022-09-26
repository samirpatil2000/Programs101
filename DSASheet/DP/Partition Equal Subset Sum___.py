class Solution:
    def target_sum(self, arr, sum):
        dp = [[False] * (sum + 1) for _ in range(len(arr) + 1)]
        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == 0 and col == 0:
                    dp[row][col] = True
                elif row == 0 :
                    dp[row][col] = False
                elif col == 0:
                    dp[row][col] = True
                else:
                    val = arr[row - 1]
                    if dp[row - 1][col]:
                        dp[row][col] = True
                    elif col >= val:
                        dp[row][col] = dp[row - 1][col - val]
        return dp[-1][-1]
                                    
    def equalPartition(self, arr, v1=0, v2=0):
        # code here
        # print(arr, v1, v2)
        # if len(arr) == 0:
        #     if v1 == v2:
        #         return True
        #     return False
        # result = self.equalPartition(arr[1:], v1 + arr[0], v2) or self.equalPartition(arr[1:], v1, v2 + arr[0])
        sum_ = sum(arr)
        if sum_ & 1 == 1:
            return False
        
        return self.target_sum(arr, sum_ // 2) 
 
arr = [1, 5, 11, 5]
# arr = [1, 0, 1]
sol = Solution()
print(sol.equalPartition(arr))