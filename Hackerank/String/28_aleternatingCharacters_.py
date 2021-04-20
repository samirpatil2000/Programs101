
def alet(s):
    i=0
    count=0
    while(i<len(s)):
        while(i<len(s)-1 and s[i]==s[i+1]):
            count+=1
            i+=1
        i+=1
    return count
    
    
    
    
    
    
s="AAABBB"
alet(s)