
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
    min=999
    max=-999
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if(str[i]==str[j]):
                count+=1
            if(count<min):
                min=count
            if(count>max):
                max=count
            # print(max,min)
    return max-min
def beuty(str):
    list=printAllSubstrings(str)
    print(list)
    count=0
    for i in list:
        if(len(i)>2):
            if l(i,len(i))> 0:
                count+=1
    return count

print(beuty("aabcbaa"))



