

from typing import Counter


def weighted(s,queries):
    i=0
    dict_={}
    while(i<len(s)):
        count=1
        while(i+1<len(s) and s[i]==s[i+1]):
            # print(count*(ord(s[i])-ord('a')+1),str(count)+str(s[i]))
            dict_[count*(ord(s[i])-ord('a')+1)]=str(count)+str(s[i])
            i+=1
            count+=1
        # if(count==1):
        dict_[count*(ord(s[i])-ord('a')+1)]=str(count)+str(s[i])
        i+=1
        
    for q in queries:
        # print(q)
        if q in dict_.keys():
            print("Yes")
        else:
            print("No")
        
    return dict_
            
s="abccddde"    
q=[1,3,12,5,9,10] 
print(weighted(s,q))