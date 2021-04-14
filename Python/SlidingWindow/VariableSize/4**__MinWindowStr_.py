
def minWindStr(string_,word):
    word_dict={char:(word.count(char)) for char in word}     
    # print(word_dict)
    count_=len(word_dict)
    i,j=0,0
    min_=2**32
    while(j<len(string_)):
        print(string_[i],i,string_[j],j,word_dict,"count = "+str(count_),"min_ "+str(min_))
        if string_[j] in word_dict:
            word_dict[string_[j]]-=1
            if word_dict[string_[j]]==0:
                count_-=1
            
            if count_==0:
                # min_=min(min_,j-i+1)
                while((string_[i] in word_dict and word_dict[string_[i]]<0) or (string_[i] not in word_dict)):
                    if(string_[i] in word_dict):
                        word_dict[string_[i]]+=1
                    i+=1
                min_=min(min_,j-i+1)
        print(string_[i],i,string_[j],j,word_dict,"count = "+str(count_),"min_ "+str(min_))

        j+=1
    return min_
   
s="totmtaptat"
w="tta"
print(minWindStr(s,w))
    