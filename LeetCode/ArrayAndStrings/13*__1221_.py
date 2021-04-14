def balanceString_(s):
    len_=len(s)
    i=0
    r_count=0
    l_count=0
    count=0
    while(i<len_):
        if(s[i]=="R"):
            r_count+=1
        if(s[i]=='L'):
            l_count+=1
        if(l_count==r_count):
            count+=1
        i+=1
    return count


s="RLRRLLRLRL"
print(s)
print(balanceString_(s))

        