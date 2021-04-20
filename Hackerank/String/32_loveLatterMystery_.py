
def l(s):
    i=0
    j=len(s)-1
    count=0
    while(i<j):
        if s[i]!=s[j]:
            count+=abs(ord(s[i])-ord(s[j]))
        i+=1
        j-=1
    
    return count


s="cba"
print(l(s))