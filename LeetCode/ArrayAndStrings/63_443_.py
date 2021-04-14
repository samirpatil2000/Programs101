
def compress(chars):
    i=0
    rep_count=0
    count=0
    str_=""
    while(i<len(chars)):
        rep_count=1
        while(i<len(chars)-1 and chars[i]==chars[i+1]):
            print(chars[i])
            rep_count+=1
            i+=1
        if(rep_count>1):    
            str_+=(str(chars[i])+str(rep_count))
            count+=2
        else:
            str_+=(str(chars[i]))
            count+=1
        i+=1
    chars=str_
    return count,chars


def withListModification(chars):
    j=0
    i=0
    unique_count=0
    while(i<len(chars)):
        count=1
        if(j!=i):
            j+=1
            chars[j]=chars[i]
        while(i<len(chars)-1 and chars[i]==chars[i+1]):
            i+=1
            count+=1
        if(count>1):
            count=str(count)
            k=0
            while(k<len(count)):
                j+=1
                chars[j]=count[k]
                unique_count+=1
                k+=1
                
        unique_count+=1
        i+=1
        
    return unique_count
    
    
    
    
chars =["a","b","b","b","b","b","b","b","b","b","b","b","b"]#["a","a","b","b","c","c","c","c","d"]
x,c=compress(chars)
# print(list(c))
# print(chars)
print(withListModification(chars))
print(chars)
