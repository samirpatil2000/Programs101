class Solution:
    def func(self, arr, n):
        hash = {}
        for i in range(n):
            hash[arr[i]] = hash.get(arr[i], 0) + 1

        for i in range(n):
            ans = n - hash[arr[i]]
            print(ans, end=' ')

n = int(input())
arr = []
for i in input().strip().split():
    arr.append(int(i))
Solution().func(arr, n)