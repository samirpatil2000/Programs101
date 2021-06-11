

import collections


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

def multi_dict(K, type):
    if K == 1:
        return collections.defaultdict(type)
    else:
        return collections.defaultdict(lambda: multi_dict(K-1, type))
y=multi_dict(2,list)


#order dict

dict_=collections.OrderedDict()
dict_[2]=None
dict_[0]=None
dict_[-1]=None

dict_[1]=None
print(dict_)

sa={}
sa[(3,4)]="sa"
print(sa)