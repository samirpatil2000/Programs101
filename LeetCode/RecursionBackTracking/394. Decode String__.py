class Solution:
    def findIndex(self,s:str,start:int):
        count_=0
        for i in range(start,len(s)):
            if s[i]=="[":
                count_+=1
            elif s[i]=="]":
                if count_==0:
                    return i-1
                else:
                    count_-=1
        return len(s)-2
    def getInt(self,s:str,start:int):
        num=""
        while start>=0 and s[start].isnumeric():
            num+=s[start]
            start-=1
        return int(num[::-1])
    
    def dfs(self,s:str,start:int,end:int):
        if start==end:
            return s[start]
        i=start
        result=""
        while i <= end:
            if s[i]=="[":
                print(s[i])
                index=self.findIndex(s,i+1)
                num=self.getInt(s,i-1)
                x=self.dfs(s,i+1,index)
                result+="".join([x]*num)
                # print(x,y,result,s[i-1])
                i=index+2
            elif s[i]==']':
                i+=1
            else:
                if s[i].isnumeric():
                    i+=1
                else:
                    result+=s[i]
                    i+=1
        return result
    def decodeString(self, s: str) -> str:
        return self.dfs(s,0,len(s)-1)
    
    
sol=Solution()
s=s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
s="100[leetcode]"
x=sol.decodeString(s)
print(x)
# print(x=="abcabccdcdcdef")