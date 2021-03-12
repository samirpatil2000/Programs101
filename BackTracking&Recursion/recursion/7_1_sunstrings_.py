list_=[]
def subStrings(string_):
    # list_=[]
    if(len(string_)==0):
        return
    for i in range(len(string_)):
        str_1=string_[:i]
        str_2=string_[i+1:]
        if(str_1):
            list_.append(str_1)
            subStrings(str_1)
        if(str_2):
            list_.append(str_2)
            subStrings(str_2)
        

print(subStrings("acd"))
print(list_)