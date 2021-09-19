



def compressionString(s:str):
    i=0
    n=len(s)
    dict_={}
    while i<n:
        k=i
        int_=""
        i+=1
        while i<n and not s[i].isalpha():
            int_+=s[i]
            i+=1
        dict_[s[k]]=dict_.get(s[k],0)+int(int_ if int_ else 1)
    result=""
    for i in sorted(dict_):
        result+=i+str(dict_[i])
    return result


s="a12b56c1"
print(compressionString(s))