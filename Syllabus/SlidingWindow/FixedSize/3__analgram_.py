
def analgram(word,string_):
    k=len(word)
    word_dict={char:(word.count(char)) for char in word}
    dict_={string_[i]:(string_[:i].count(string_[i])+1) for i in range(k)}
    # print(word_dict)
    
    count=0
    print(len(string_),k)
    for i in range(len(string_)-k):
        # print(dict_)
        if(word_dict==dict_):
            # print(i,string_[i],word_dict,dict_)
            count+=1
        if string_[i] in dict_:
            dict_[string_[i]]-=1
            if(dict_[string_[i]]==0):
                dict_.pop(string_[i])
        # print(dict_)
        print("i+k",i+k)
        if string_[i+k] in dict_:
            dict_[string_[i+k]]+=1
        else:
            dict_[string_[i+k]]=1
        # print(dict_)
        print(i)

    
    print(dict_)
    
    return count

    # for i in range():
    #     return
    
        
    
w="aaba"
s="aabaaabaa"
print(analgram(w,s))