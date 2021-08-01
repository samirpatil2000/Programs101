


def uniqueMorseRepresentations(words):
    list_=[".-","-...","-.-.","-..",".","..-.","--.","....",".."
           ,".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
           "...","-","..-","...-",".--","-..-","-.--","--.."]
    return_list=[]
    count=0
    for word in words:
        str_=""
        for i in range(len(word)):
            str_+=list_[ord(word[i])-97]

        if(str_ not in return_list):
            count+=1
            return_list.append(str_)
    return count

words=["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
            
             

