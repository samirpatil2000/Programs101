
# def printAllSubstrings(s):
#     list=[]
#     for i in range(len(s)):
#         temp=""
#         for j in range(i,len(s)):
#             temp+=s[j]
#             list.append(temp)

#     return list

# def l(str,n):
#     # count=1
#     min=999
#     max=-999
#     for i in range(n):
#         count=1
#         for j in range(i+1,n):
#             if(str[i]==str[j]):
#                 count+=1
#             if(count<min):
#                 min=count
#             if(count>max):
#                 max=count
#             # print(max,min)
        
#     return max-min

# def beuty(list):
#     count=0
#     for i in list:
#         if l(i,len(i))> 0:
#             count+=1
    
#     return count
            
            

# stri="abcb"




# print(l(stri,len(stri)))





def printAllSubstrings(s):
        list=[]
        n=len(s)
        for i in range(n):
            temp=""
            for j in range(i,n):
                temp+=s[j]
                list.append(temp)
        return list
def l(str,n):
    # count=1
    s_list=[]
    for i in str:
        s_list.append(i)
    min=999
    max=-999
    for i in range(n):
        if(s_list[i] !="$"):
            count=1
            for j in range(i+1,n):
                if(s_list[j] != "$"):
                    if(s_list[i]==s_list[j]):
                        count+=1
                        s_list[j]="$"
                    # l_=[count,str[i]]
                    # list_.append(l_)
                    # print(str)
                    # print(max,min)
            s_list[i]="$"   
            if(count<min):
                min=count
            if(count>max):
                max=count
    return max-min

def getsubString(str_):
    if(len(str_)==0):
        return []
    ch=str_[0]
    rem=str_[1:]
    list_=getsubString(rem)
    list_.append(ch)
    list_.append(rem)
    list_.append(ch+rem)
    return list_


print(getsubString("aabcbaa"))

def beuty(str):
    list=printAllSubstrings(str)
    print(list)
    print(len(list))
    count=0
    for i in list:
        if(len(i)>1):
            if l(i,len(i)) > 0:
                print(i,"=",l(i,len(i)))
                count+=1
    return count

s="aabcbaa"
print(beuty(s))



# print(l(s,len(s)))



