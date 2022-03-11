from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 1
        curr_sum = nums[0]
        ans = 0
        while j < len(nums) and i <= j:
            print(curr_sum, j, i)
            if curr_sum == k:
                curr_sum -= nums[i]
                ans += 1
                i += 1
            elif curr_sum > k:
                curr_sum -= nums[i]
                i += 1
            else:
                curr_sum += nums[j]
                j += 1
        return ans

sol = Solution()
nums = [1,1,1]
k = 2

print(sol.subarraySum(nums, k))