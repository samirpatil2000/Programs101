from typing import List
import bisect

class Solution:
    def binarySearch(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid][0] == target:
                return mid
            elif nums[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if nums[left][0] == target else -1
    def jobScheduling(self,startTime,endTime,profit)->int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            print(dp)
            print(i,s,[s+1],i-1)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        print(dp)
        return dp[-1][1]
            
sol=Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
# startTime = [1,2,3,4,6]
# endTime = [3,5,10,6,9]
# profit = [20,20,100,70,60]

# startTime = [4,2,4,8,2]
# endTime = [5,5,5,10,8]
# profit = [1,2,8,10,4]


# print(sol.jobScheduling(startTime,endTime,profit))                    
print(sol.jobScheduling(startTime,endTime,profit))                    
        

"""def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startTime=list(zip(startTime,endTime,profit))
        startTime.sort()
        print(startTime)
        def dfs(n=startTime[0][0],dict_={},len_=len(startTime)):
            print(dict_)
            # if n in dict_:return dict_[n]
            index=self.binarySearch(startTime,n)
            if index==-1:
                dict_[n]=-1
                return 0
            index_list=[index]
            i=index+1
            while i<len_ and startTime[i][0]==startTime[index][0]:
                index_list.append(i)
                i+=1
            print(n,index_list)

            with_index=dfs(startTime[index_list[0]][1],dict_)+startTime[index_list[0]][2]
            for index in index_list[1:]:
                with_index=max(dfs(startTime[index][1],dict_)+startTime[index][2],with_index)
            without_index=dfs(n+1,dict_)
            dict_[n]=max(with_index,without_index)
            return dict_[n]
        return dfs()
    """