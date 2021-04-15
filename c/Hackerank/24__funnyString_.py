
def funnyString(s):
    i=0
    j=len(s)-1
    while(i<len(s)):
        if(j>=1 and i<len(s)-1 and abs(ord(s[i])-ord(s[i+1]))!=abs(ord(s[j])-ord(s[j-1])) ):
            return "Not Funny"
        i+=1
        j-=1
        
    return "Funny"


s="lmnop"
print(funnyString(s))
            