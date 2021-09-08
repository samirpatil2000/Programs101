from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n=len(shifts)
        for i in range(n-2,-1,-1):
            shifts[i]+=shifts[i+1]
        result=""
        for j in range(n):
            print(s[j],ord(s[j]),shifts[j]%25)
            result+=chr(((ord(s[j])-97)+shifts[j])%26+97)
        #     print(result)
        return result
        # print(chr(ord("a")+(ord("a")+3)%25))
        

sol=Solution()

s,shifts="abc",[3,5,9]
s,shifts="bad",[10,20,30] #"jyh"
# s = "yyy"
# shifts = [1,2,3]
print(sol.shiftingLetters(s,shifts))
print(ord("j"))

        