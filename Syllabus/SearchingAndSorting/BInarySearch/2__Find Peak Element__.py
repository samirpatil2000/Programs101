from typing import List


class Solution:
    
    def find_peak_element(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (left + right) // 2
            print(left, right, mid)
            next_to_mid = nums[mid + 1] if mid < len(nums) - 1 else -2 ** 32
            if nums[mid] > next_to_mid:
                return nums[mid]
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid
        return nums[-1]

    
    

    
    
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right - left > 0:
            mid = (left + right)//2
            right_ = nums[mid + 1] if mid + 1 < len(nums) else -2**32
            if nums[mid] > right_:
                right = mid
            else:
                left = mid+1
        return nums[left]
    
    
    
    
    
    
    
    
        


nums = [1,2,3,1]
nums = [-1,0,2]
nums = [0, 1, 2, 3]
sol = Solution()
print(sol.findPeakElement(nums))
print(sol.find_peak_element(nums))