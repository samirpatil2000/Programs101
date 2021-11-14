import collections
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dict_={}
        arr.sort()
        for i in arr:
            dict_[i]=dict_.get(i,0)+1
        for e in dict_:
            if dict_[e]>0:
                target=2*e if e>0 else e//2
                if e<0 and abs(e)%2!=0:
                    return False
                if dict_[e]>dict_.get(target,0):
                    return False
                dict_[target]-=dict_[e]
        return True
    def canReorderDoubled3(self, arr: List[int]) -> bool:
        hash_map={}
        arr.sort()
        for el in arr:
            hash_map[el]=hash_map.get(el, 0)+1
        
        target=0
        for el in hash_map:
            if hash_map[el]>0:
                target=2*el if el>0 else el//2

                if el <0 and abs(el)%2!=0:
                    return False

                if hash_map[el]> hash_map.get(target, 0):
                    return False

                hash_map[target]=hash_map[target]-hash_map[el]
            
        return True
    
    def canReorderDoubled2(self, A):
        cnt = collections.Counter(A)
        print(cnt)
        for a in sorted(A, key = abs):
            if cnt[a] and cnt[a * 2]:
                cnt[a] -= 1
                cnt[a * 2] -= 1  
        print(cnt)
        return all(cnt[a] == 0 for a in A)    
        
sol=Solution()
arr=[4,-2,2,-4]
# arr=[1,2,4,16,8,4]
# # arr=[3,1,3,6]
# arr=[2,1,2,6]
# arr=[0,0,0,0]
# arr=[-2,-1,-4,-2,-1,-3,-2,-6]
print(sol.canReorderDoubled(arr))
# print(3/2)
# print(sol.canReorderDoubled2(arr))
print(sol.canReorderDoubled3(arr))
# print(3/2)