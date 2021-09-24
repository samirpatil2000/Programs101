class Solution:
    def breakPalindrome(self, s: str) -> str:
        s=list(s)
        if len(s)==1:
            return ""
        n=len(s)
        mid=len(s)//2
        last=True
        for i in range(n):
            if i==mid and n%2!=0:
                continue
            if s[i]=='a':
                continue
            
            s[i]='a'
            last=False
            break
        if last:
            s[-1]="b"
        return "".join(s)

sol=Solution()
s="abccba"
s="aba"
print(sol.breakPalindrome(s))
            
                
                