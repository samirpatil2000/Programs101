from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict_={}
        for i in arr:
            if i in dict_:dict_[i]+=1
            else:dict_[i]=1
        # print(sorted(dict_.items(),key=lambda x:x[1],reverse=True))
        total_sum=0
        count_=0
        for u,v in sorted(dict_.items(),key=lambda x:x[1],reverse=True):
            total_sum+=v
            count_+=1
            if total_sum>=len(arr)//2:
                return count_
            
        
        
sol=Solution()
arr = [3,3,3,3,5,5,5,2,2,7]
arr = [7,7,7,7,7,7]
arr = [1,9]
arr = [1000,1000,3,7]
arr = [1,2,3,4,5,6,7,8,9,10]
print(sol.minSetSize(arr))