
class Solution:
    
    def update_array(self, arr, query):
        diff_arr = [0] * (len(arr) + 1) 
        diff_arr[0] = arr[0]
        for i in range(1, len(arr)):
            diff_arr[i] = arr[i] - arr[i - 1]
        print(diff_arr)
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += diff_arr[i]
            print(curr_sum)

sol = Solution()
arr = [2, 5, 7, 10, 15, 16, 13]
query = []
print(sol.update_array(arr, query))


#       1
# 7
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# 1 3 8 6 4 6 2      


# 6
# 10
# 1 3
# 2 10
# 3 9
# 4 5
# 5 2
# 6 3
# 7 3
# 8 3
# 9 4
# 78 61 91 63 9 68 23 45 96 66
# 8
# 1 7
# 2 8
# 3 7
# 4 8
# 5 1
# 6 3
# 7 4
# 73 93 100 19 17 86 61 25
# 8
# 1 3
# 2 8
# 3 6
# 4 5
# 5 8
# 6 7
# 7 8
# 56 4 72 26 56 98 25 98
# 9
# 1 7
# 2 5
# 3 7
# 4 8
# 5 9
# 6 9
# 7 6
# 8 6
# 80 24 90 8 22 8 74 2 8
# 9
# 1 3
# 2 1
# 3 9
# 4 9
# 5 7
# 6 7
# 7 4
# 8 3
# 32 84 84 59 9 44 37 97 89
# 10
# 1 6
# 2 5
# 3 2
# 4 5
# 5 10
# 6 8
# 7 4
# 8 5
# 9 10
# 46 46 13 93 87 50 30 29 74 56
# 8 5
# 6 4
# 4 3
# 0 0
# 7 5
# 7 5
