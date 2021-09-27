
def repetation(s:str):
    i=0
    max_=0
    while i<len(s):
        count_=1
        while i<len(s)-1 and s[i]==s[i+1]:
            i+=1
            count_+=1
        max_=max(count_,max_)    
        i+=1
    return max_

s=input()
print(repetation(s))
