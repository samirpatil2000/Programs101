def LIS(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
    # [1,  1, 1, 1+1, 1+1, 2+1,   1, 1]
arr = [10, 9, 2, 5, 3, 7,       101, 18]
print(LIS(arr))
            