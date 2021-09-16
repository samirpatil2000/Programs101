
def encryption(s,e):
    len_s=len(s)
    arr=[0]*len_s
    for i in range(len_s):
        arr[i]=ord(s[i])-ord("a")
    len_e=len(e)
    i=0
    result=""
    while i<len_e:
        result+=chr(((ord(e[i])+arr[i%len_s])-ord("a"))%26+ord("a"))
        i+=1
    return result


s=input()
e=input()
print(fun(s,e))