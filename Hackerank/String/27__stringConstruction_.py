
def strngCn(s):
    # dict_={ch:(s.count(ch)) for ch in s}
    dict_={}
    count=0
    for ch in s:
        if ch in dict_:
            dict_[ch]+=1
        else:
            dict_[ch]=1
            count+=1
    print(dict_,count)
    return count
    


s="abcabc"
strngCn(s)
    