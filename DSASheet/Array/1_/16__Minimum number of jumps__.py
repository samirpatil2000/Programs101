class Solution:
    	def minJumps(self, arr):
	    #code here
            arr[-1] = 0
            for i in range(len(arr) - 2, -1, -1):
                min_jumps = 2**32
                if arr[i] == 0:
                    arr[i] = min_jumps
                    continue
                jumps = arr[i]
                for j in range(i + 1, min(i + 1 + jumps, len(arr))):
                    min_jumps = min(arr[j] + 1, min_jumps)
                    if min_jumps == 1:
                        break
                arr[i] = min_jumps
            print(arr)
            return -1 if arr[0] >= 2**32 else arr[0]
        
sol = Solution()
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [2, 2, 8, 2, 6, 7]
print(sol.minJumps(arr))

# for j in range(1, 1):
    