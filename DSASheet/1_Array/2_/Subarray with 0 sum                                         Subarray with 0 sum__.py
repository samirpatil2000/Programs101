class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n = 0):
        
        set_ = set()
        set_.add(arr[0])
        for i in range(1, len(arr)):
            
            if arr[i] == 0 or arr[i - 1] == 0:
                return True
            arr[i] += arr[i - 1]
            if arr[i] == 0 or arr[i] in set_:
                return True
            set_.add(arr[i])
        return False
    
    
sol = Solution()
arr = [4, -4]
print(sol.subArrayExists(arr))
    