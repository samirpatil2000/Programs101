

word="aaabscsdsd"
word_dict={char:(word.count(char)) for char in word}

print(word_dict)


string_="anc"
# for i in range(len(string_)):
#     if string_[i] in word_dict:
#         word_dict[word_dict[i]]-=1
#         if(word_dict[string_[i]]==0):
#             word_dict.pop(string_[i])
            
# for i in word_dict.values():
#     print(i)
    
# for key,values in word_dict.items():
#     print(key,values)
    
key_value={8: [0], 1: [1], 2: [2, 3], 3: [4]}
for i in sorted (key_value) :
    print ((i, key_value[i]), end =" ")
    
    
dictionary = dict()
dictionary[1] = dict()
dictionary[1][1] = 3
print(dictionary[1][1])


arr=[2,3,4,5]
print(arr.index(max(arr)))