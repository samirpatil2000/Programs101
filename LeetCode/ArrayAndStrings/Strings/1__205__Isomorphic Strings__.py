from typing import Tuple


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_={}
        count_=0
        arr=[]
        for i in s:
            if i not in dict_:
                dict_[i]=count_
                count_+=1
            arr.append(dict_[i])
        dict_={}
        count_=0
        index=0
        for i in t:
            if i not in dict_:
                dict_[i]=count_
                count_+=1
            if arr[index]!=dict_[i]:return False                
            index+=1
        return True
sol=Solution()
s = "baba"
t = "badc"
# s = "paper"
# t = "title"
print(sol.isIsomorphic(s,t))
            
                
        