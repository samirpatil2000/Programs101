from re import A
from typing import List
from unittest import result


class Solution:
    def union_of_arr(self, arr1:List[int], arr2:List[int]):
        if len(arr1) == 0:
            result = set(arr1)
        elif len(arr2) == 0:
            result = set(arr2)
        else:
            result = set(arr1)
            result.update(set(arr2))
        return len(result)
        # result = -1
        # ans = 0
        # i, j = 0, 0
        # arr1.sort()
        # arr2.sort()
        # while i < len(arr1) and j < len(arr2):
        #     if arr1[i] == arr2[j]:
        #         if arr2[j] != result:
        #             ans += 1
        #             result = arr2[j]
        #         i += 1
        #         j += 1
        #     elif arr1[i] > arr2[j]:
        #         if arr2[j] != result:
        #             ans += 1
        #             result = arr2[j]
        #         j += 1
        #     else:
        #         if arr1[i] != result:
        #             ans += 1
        #             result = arr1[i]
        #         i += 1
        # for ele in range(i, len(arr1)):
        #     if arr1[ele] != result:
        #         ans += 1
        #         result = arr1[ele]
        
        # for ele in range(j, len(arr2)):
        #     if arr2[ele] != result:
        #         ans += 1
        #         result = arr2[ele]
        return ans
                
            
sol = Solution()
arr1, arr2 = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
print(sol.union_of_arr(arr1, arr2))
# arr1 = [int(i) for i in input().split()]
# arr2 = [int(i) for i in input().split()]

# print(arr1)
# print(arr2)