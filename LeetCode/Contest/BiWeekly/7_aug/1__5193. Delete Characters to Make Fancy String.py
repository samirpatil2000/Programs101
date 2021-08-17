class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        s=list(s)
        i=0
        while i<n:
            j=i
            count_=0
            while j<n-1 and s[j]==s[j+1]:
                j+=1
                count_+=1
            if count_>=2:
                del s[i+2:i+count_+1]
                n=len(s)
            i+=1
        return ''.join(s)
    
sol=Solution()
# print(sol.makeFancyString('leeetcode'))
import random
x=random.randint(97,122)
print(chr(x))