class Solution:
    
    
    def find_left_min(self, arr):
        left_min = []
        st = [-1]
        for i in range(len(arr)):
            while st[-1] != -1 and arr[i] <= arr[st[-1]]:
                st.pop()
            left_min.append(st[-1])
            st.append(i)
        return left_min
    
    def find_right_min(self, arr):
        n = len(arr)
        right_min = [n] * (n)
        st = [n]
        for i in range(n - 1, -1, -1):
            while st[-1] != n and arr[i] <= arr[st[-1]]:
                st.pop()
            right_min[i] = st[-1]
            st.append(i)
        return right_min     
            
    def largetArea(self, arr):
        left_min = self.find_left_min(arr)
        right_min = self.find_right_min(arr)
        result = -1
        for i in range(len(arr)):
            result = max(result, (right_min[i] - left_min[i] - 1) * arr[i])
        return result
        
        
arr = [2, 5, 6, 2, 4, 2, 1, 3, 4]
arr = [6,2,5,4,5,1,6]
arr = [7, 2, 8, 9, 1, 3, 6, 5]
sol = Solution()
print(sol.largetArea(arr))