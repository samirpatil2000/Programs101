import bisect


class Solution:
    def kthSmallest(self, mat, k):
        left = mat[0][0]
        right = mat[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            less_than_mid = 0
            for i in range(len(mat)):
                less_than_mid += bisect.bisect(mat[i], mid)
            if less_than_mid < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
sol = Solution()
mat =     [ [ 16, 28, 60, 64] ,
            [ 22, 41, 63, 91] ,
            [ 27, 50, 87, 93] ,
            [ 36, 78, 87, 94 ] ] 
k = 3
mat = [[10, 20, 30, 40],
                   [15, 25, 35, 45],
                   [24, 29, 37, 48],
                   [32, 33, 39, 50]]
k = 7

print(sol.kthSmallest(mat, k))