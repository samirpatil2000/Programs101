def reverseStr(str_,len_):
    left=0
    right=len(str_)-1
    str_2=[]
    for s in str_:str_2.append(s)
    while(left<right):
        temp=str_2[left]
        str_2[left]=str_2[right]
        str_2[right]=temp
        left+=1
        right-=1
    str_=""
    for s in str_2:str_+=s
    return str_


def reverseWord(s):
    i=0
    str_1=""
    while(i<len(s)):
        str_2=""
        len_count=0
        while(i<len(s) and s[i]!=" "):
            str_2+=s[i]
            i+=1
            len_count+=1
        str_1+=reverseStr(str_2,len_count)
        if(i<len(s)):
            str_1+=" "
        i+=1
    return str_1

print(reverseWord("HIi the"))