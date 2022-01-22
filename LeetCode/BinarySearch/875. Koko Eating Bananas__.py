



from typing import List
import bisect

class Solution:
    
    
    def totalHours(self, arr: List[int], target: int, h: int):
        count_ = 0
        for p in arr:
            count_ += p // target
            if p % target != 0:
                count_ += 1
        return count_ <= h
        
        # prev_val = 0
        # ans = 0
        # i = 1
        # first_time = False
        # while target != max_:
        #     curent_less_element = bisect.bisect(arr,target)
        #     ans += (target * (curent_less_element - prev_val))
        #     prev_val = curent_less_element
        #     target *= i
        #     i += 1
        #     if target > max_:
        #         if first_time:
        #             break
        #         first_time = True
        # return ans
        
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        # arr.sort()
        low = 1
        high = max(arr)
        while low < high:
            mid = (low + high) // 2
            if not self.totalHours(arr, mid, h):
                low = mid + 1
            else:
                high = mid 
        return low

sol = Solution()
arr, h = [3, 6, 7, 11], 8
arr, h = [30, 11, 23, 4, 20], 6

print(sol.minEatingSpeed(arr, h))
