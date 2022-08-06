from typing import List


class Solution:
    
    
    def find_max_index(self, arr):
        ans = 0 
        for i in range(len(arr)):
            if int(arr[ans]) < int(arr[i]):
                ans = i
        return ans
    
    def slotWheels(self, history:List[str]):
        result = 0
        for _ in range(len(history[0])):
            ans = 0
            for i in range(len(history)):
                history[i] = list(history[i])
                index = self.find_max_index(history[i])
                ans = max(int(history[i][index]), ans)
                history[i][index] = "0"
            result += ans
        return result
    

    
sol = Solution()
arr = ["712", "246", "365", "312"]
arr = ["137"
,"115",
"364",
"115",
"724"]
print(sol.slotWheels(arr))