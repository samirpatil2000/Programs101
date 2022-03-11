class Solution:
    def sort012(self,arr,n):
        # code here
        start = 0
        end = n- 1
        mid = 0
        while mid <= end:
            if arr[mid] == 0:
                arr[mid], arr[start] = arr[start], arr[mid]
                start += 1
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end -= 1
            else:
                mid += 1
                
n = [int(x) for x in input().strip().split()]

sol = Solution()
sol.sort012(n, len(n))
print(n)
