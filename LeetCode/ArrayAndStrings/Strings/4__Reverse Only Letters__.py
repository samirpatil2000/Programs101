class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        new_s=list(s)
        i,j=0,n-1
        while i<n and j>=0:
            if s[i].isalpha() and s[j].isalpha():
                new_s[i]=s[j]
                i+=1
                j-=1
            elif s[i].isalpha():
                j-=1
            elif s[j].isalpha():
                i+=1
            else:
                j-=1
                i+=1
        return "".join(new_s)
    
sol=Solution()
s="a-bC-dEf-ghIj"
print(sol.reverseOnlyLetters(s))