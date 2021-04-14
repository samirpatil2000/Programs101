
def reserveString(s):
    left=0
    right=len(s)-1
    while(left<right):
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

def reverseFun(s,k):
    s=[str(i) for i in s]
    i=0
    new_str=[]
    while(i<len(s)):
        new_str+=reserveString(s[i:i+k])
        new_str+=s[i+k:i+2*k]
        i+=k
        i+=k
        
    return_str=""
    for i in new_str:
        return_str+=i
    return return_str 
    

string_="bacdfeg"
s_list=[str(i) for i in string_]
print(reverseFun(string_,2))
