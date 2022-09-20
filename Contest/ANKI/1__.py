

# # # def remove_string():
# # #     s1 = input()
# # #     ans = ""
# # #     s2_set  = set(input())
# # #     for i in range(len(s1)):
# # #         if s1[i] in s2_set:
# # #             continue
# # #         ans += s1[i]
# # #     return ans

# # # print(remove_string())


import collections
class Solution:
    def dfs(self, mat, src_row, src_col, ones=[]):
        mat[src_row][src_col] = -1
        dr = [+1, 0, -1, 0]
        dc = [ 0, -1, 0, +1]
        for i in range(4):
            row, col = src_row + dr[i], src_col + dc[i]
            if row < 0 or col < 0:
                continue
            if row >= len(mat) or col >= len(mat[0]):
                continue
            if mat[row][col] == -1 or mat[row][col] == 0:
                continue
            ones[0] += 1
            self.dfs(mat, row, col, ones)
            
    def numIslands(self, grid):
        ans = 0
        turn = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1 or grid[row][col] == 0:
                    continue
                ones = [0]
                self.dfs(grid, row, col, ones)
                # if turn != 0 or turn & 1 == 1: 
                #     ans +=  ones[0]
        return ans
    
# # sol = Solution()
# # n, m = map(int, input().strip().split())
# # grid = []
# # for i in range(n):
# #     grid.append(list(map(int, input().strip().split())))
# # print(sol.numIslands(grid))


# # 2 2
# # 1 1
# # 1 1

#     # n = len(str)
#     # while n - 1:
#     #     str = str[1:] + str[0]
#     #     print(str, end=" ")
#     #     n -= 1
        

# # findPowers("56743")



# from re import X


# class Solution:
    
#     def find_min_element(self, arr_set, n):
#         if not arr_set:
#             return 1
#         for i in range(1, n + 1):
#             if i not in arr_set:
#                 return i
#         return 0
                           
    
#     def dfs(self, arr, min_, n, out=[], result=0):
#         if len(arr) == 0 :
#             x = set(out)
#             result[0] += self.find_min_element(x, n)
#             result[1] += min_
#             print(out, result)
#             return 
#         if min_ == 
#         self.dfs(arr[1:], n, out + [arr[0]], result)
#         self.dfs(arr[1:], n, out, result)
        
#     def input(self):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         result = [0, 0]
#         min_ = 1
#         self.dfs(arr, min_, n, [], result)
#         return result[0]
        
        

# sol  = Solution()
# # print(sol.dfs([1, 2, 1]), )
# # arr = [1, 2, 1]    
# # x = set(arr)
# # print(sol.find_min_element(x, len(arr)))

# print(sol.input())


import math
 
# A function to find largest prime factor\
class Solution:
    
    @classmethod
    def max_prime_factor(cls, n):
        max_prime = -1   
        while n % 2 == 0:
            max_prime = 2
            n >>= 1               
        while n % 3 == 0:
            max_prime = 3
            n=n/3
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            while n % i == 0:
                max_prime = i
                n = n / i
            while n % (i+2) == 0:
                max_prime = i+2
                n = n / (i+2)
        if n > 4:
            max_prime = n
        return int(max_prime)
    
    @classmethod
    def reduction(cls,  n):
        counter = 0
        while n != 0:
            max_prime = cls.max_prime_factor(n)
            if max_prime > 1:
                n -= max_prime
            else:
                n -= 1
            counter += 1          
        return counter + 1
    

# sol = Solution()
# print(sol.reduction(1))
    
    
class Solution:
    
    def result(self, arr):
        for i in range(len(arr)):
            print(arr[i:])
            # for j in range(i, len(arr)):
            #     print(arr[i:])
    
#     def result(self, arr):
#         dict_ = {"odd_min": 2**32, "even_min": 2**32, "odd_max": -1, "even_max": -1 }
#         for i in range(len(arr)):
#             if arr[i] % 2 == 0:
#                 dict_["even_min"] = min(dict_["even_min"], arr[i])
#                 dict_["even_max"] = max(dict_["even_max"], arr[i])
#             else:
#                 dict_["odd_min"] = min(dict_["odd_min"], arr[i])
#                 dict_["odd_max"] = max(dict_["odd_max"], arr[i])
#         return (dict_["odd_max"] - dict_["odd_min"]) + (dict_["even_max"] - dict_["even_min"])

# arr = [1, 3, 6, 8, 2, 6, 8]             
# print(Solution().result(arr))
    
#     def find(self, N, password):
#         dp = [[0] * 50 for _ in range(N)]
#         for row in range(N):
#             for col in range(50):
#                 if row == 0 and col == 0:
#                     dp[row][col] = 5000
#                 elif col == 0:
#                     dp[row][col] = 5000 * (row + 1)
#                 else:
#                     dp[row][col] = dp[row][col - 1] + col + 5000
#                 if dp[row][col] == password:
#                     return col + 1
#         return -1                

# print(Solution().find(1, 5000))

# print(Solution().result(["A", "B", "C", "D"]))
# arr = [True, True, False, False]
# print(sorted(arr, key=lambda x: -x))

def fun(productIDs):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = 0
    for id in productIDs:
        if id not in vowels:
            result += 1
    return result
        
        
def primeFactors(n):
     
    result = 0
    while n % 2 == 0:
        if not result:
            result += 2
        n = n // 2
         
    for i in range(3, int(math.sqrt(n))+1, 2):
         
        while n % i == 0:
            result += i
            print(i)
            n = n // i
            
    if n > 2:
        result += n
        print(n)
    return int(result) 

print(primeFactors(120))