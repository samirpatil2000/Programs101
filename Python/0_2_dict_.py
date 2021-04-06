

word="aaabscsdsd"
word_dict={char:(word.count(char)) for char in word}

print(word_dict)


string_="anc"
for i in range(len(string_)):
    if string_[i] in word_dict:
        word_dict[word_dict[i]]-=1
        if(word_dict[string_[i]]==0):
            word_dict.pop(string_[i])