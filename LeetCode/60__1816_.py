def truncateSentence(s, k):
    s=[str(i) for i in s]
    count=0
    str_=""
    for i in range(len(s)):
        
        if(s[i]==" "):
            count+=1
        if(count==k):
            break
        str_+=s[i]
    return str_


s = "chopper is not a tanuki"
k = 5

print(truncateSentence(s,k))
    
    