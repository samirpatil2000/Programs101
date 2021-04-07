
def longestSubString(string_):
    list_=[string_[0]]
    i=0
    j=1
    max_=1
    while(j<len(string_)):
        list_.append(string_[j])
        k=len(list_)-2
        # print("k = ",k ,string_[j], string_[k])
        while(k>0 and string_[j] != list_[k]):
            k-=1
        
        if(k>=0 and string_[j]==list_[k]):
            print(list_ ,k,j)
            list_=list_[k+1:]
            print(list_,10000)
        
        print("count = j ",j,string_[j])
        max_=max(len(list_),max_)
        print(list_,"#",string_[j]," max_",max_)
        j+=1
    return max_

def anotherApproach(string_):
    i=0
    j=0
    max_=1
    dict_={}
    while(j<len(string_)):
        dict_[string_[j]]=1
        print(dict_,max_,j-i+1,i)
        if len(dict_)==j-i+1:
            max_=max(j-i+1,max_)
        elif(len(dict_)<j-i+1):
            while(len(dict_)>0 and i<len(string_) and len(dict_)<j-i+1 ):
                # print(dict_)
                print(string_[i])
                dict_.pop(string_[i])
                i+=1
                print(dict_)
        j+=1
    return max_

str_="pwwkeq"
# print(longestSubString(str_))
print(anotherApproach(str_))
        