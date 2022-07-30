class Solution:
    def smallestSubWithSum(self, a, x):
        # Your code goes here 
        min_length = 2**32
        start = 0
        end = 0
        current_sum = 0
        while end <= len(a):
            if start == end and end != len(a):
                if current_sum > x:
                    return 1
                current_sum += a[end]
                end += 1
                continue
            if current_sum > x:
                min_length = min(min_length, end - 1 - start + 1)
                current_sum -= a[start]
                start += 1
            else:
                if end < len(a):
                    current_sum += a[end]
                end += 1
        return min_length

sol = Solution()
A = [1, 4, 45, 6, 0, 19]
x  =  51
A = [1, 5, 2, 7, 10]
x = 9
print(sol.smallestSubWithSum(A, x))