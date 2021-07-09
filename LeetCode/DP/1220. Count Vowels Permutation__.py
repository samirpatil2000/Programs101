from typing import Dict


class Solution:
    def validPosition(self,valid_position_dict:Dict,prev_arr:Dict,key:str)->int:
        count_=0
        for i in prev_arr.keys():
            if key in valid_position_dict[i]:
                count_+=prev_arr[i]        
        return count_
        
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        valid_position_dict={
            'a':('e'),
            'e':('a','i'),
            'i':('a','e','o','u'),
            'o':('i','u'),
            'u':('a'),
        }
        prev_arr={'a':1,'e':1,'i':1,'o':1,'u':1}
        
        for _ in range(1,n):
            curr_arr={'a':1,'e':1,'i':1,'o':1,'u':1}
            
            for j in prev_arr.keys():
                curr_arr[j]=self.validPosition(valid_position_dict,prev_arr,j)
            prev_arr=curr_arr
        return sum(prev_arr.values())%mod,prev_arr.values()
    
sol=Solution()
n=144
print(sol.countVowelPermutation(n))
