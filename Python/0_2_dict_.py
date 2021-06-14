

import collections


class Dictionary():
    def __init__(self) -> None:
        self.word_dict={}
        
    def countChar(self):
        word="aaabscsdsd"
        word_dict={}
        for ch in word:
            word_dict[ch]=word.count(ch)
        
        # one liner  
        word_dict={char:(word.count(char)) for char in word}
        self.word_dict=word_dict
        return word_dict
    
    
    def printItemsValuesKeys(self):
        print("Keys")
        for i in self.word_dict.values():
            print(i,end=" ")
        # print
        print("\nkeys Values")
        for key,values in self.word_dict.items():
            print(key,values,end=" , ")
            
    def removeFromDict(self):
        word_dict={}
        string_="anc"
        for i in range(len(string_)):
            if string_[i] in word_dict:
                word_dict[word_dict[i]]-=1
                if(word_dict[string_[i]]==0):
                    word_dict.pop(string_[i])
                    
                    
    def sorting(self):
        key_value={8: [0], 1: [1], 2: [2, 3], 3: [4]}
        for i in sorted (key_value) :
            print ((i, key_value[i]), end =" ")
    
    def muiltiDict(self):
        dictionary = dict()
        dictionary[1] = dict()
        dictionary[1][1] = 3
        print(dictionary," , ",dictionary[1], " , ",dictionary[1][1])
        
        
    def multiDictUsingRecursion(self):
        def multi_dict(K, type):
            if K == 1:
                return collections.defaultdict(type)
            else:
                return collections.defaultdict(lambda: multi_dict(K-1, type))
        y=multi_dict(2,list)
        print(y)
        
    def orderDict(self):
        dict_=collections.OrderedDict()
        dict_[2]=None
        dict_[0]=None
        dict_[-1]=None

        dict_[1]=None
        print(dict_)
        
    def sortingAccKeyValue(self):
        arr=[1,2,1,2,6]
        dict_={}
        def fun(arr):
            
            for i in arr:
                if i in dict_:
                    dict_[i]+=1
                else:
                    dict_[i]=1
            # list_=zip(dict_.values(),dict_.keys())
            # list_=sorted(list_,reverse=True)
            for i in sorted(zip(dict_.values(),dict_.keys()),reverse=True):
                print(i[1],end=" ")
            print()
            
            print("OR")
            # for i in sorted()
            sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
            print(sort_orders)
            sort_orders = sorted(zip(orders.values(),orders.keys()), reverse=True)
            print(sort_orders)
        fun(arr)
        
orders = {
	2: 54,
	3: 56,
	1: 72,
	4: 48,
	5: 72
}
            
sol=Dictionary()
# print(sol.countChar())
# sol.printItemsValuesKeys()
# sol.muiltiDict()
# sol.multiDictUsingRecursion()
sol.sortingAccKeyValue()

            

