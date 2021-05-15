str_="samir"

print(str_[:len(str_)-1])
print(str_[-1])


def sortSentence(str_):
    dict_={}
    i=0
    while i<len(str_):
        word=" "
        while i<len(str_) and str_[i]!=" ":
            word+=str_[i]
            i+=1
        dict_[int(word[-1])]=word[1:len(word)-1]
        i+=1
    # print(dict_)
    res=""
    for i in sorted(dict_.keys()):
        res+=str(dict_[i])
        res+=" "
    return res[:len(res)-1]
    
s="Myself2 Me1 I4 and3"
print(sortSentence(s))