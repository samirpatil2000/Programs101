

def pickToy(s):
    i=0
    j=0
    dict_={}
    max_=0
    while(j<len(s)):            
        if(s[j] in dict_ and len(dict_)<=2):
            dict_[s[j]]+=1
        elif(len(dict_)<2):
            dict_[s[j]]=1
        else:
            while(len(dict_)==2):
                dict_[s[i]]-=1
                if(dict_[s[i]]==0):
                    dict_.pop(s[i])
                i+=1
            if(len(dict_)<=2):
                dict_[s[j]]=1
        print(dict_,s[j])
        j+=1
        max_=max(max_,sum(dict_.values()))
        
    return max_


str_="abaccab"

print(pickToy(str_))
    