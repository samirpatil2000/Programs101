s="aabcbaa"
# a=dict.fromkeys(s,s.count())
# print(a)
# co=
# print(co)
sa={char:(s.count(char)) for char in s}
print(sa)

print(ord("a"),ord("A"))
print(chr(97))


def dicto():
    dict_={'a': 2, 'b': 1, 's': 1}
    dict_['a']-=1
    print(dict_['a'],dict_.values)
    dict_['k']=2
    print(dict_)
    return

# dicto()

def pangram():
    word_dict={chr(i):0 for i in range(65,91)}
    
    word_dict.update({chr(i):0 for i in range(97,123)})
    print(word_dict)
    
    
# pangram()
print(ord("A"),ord("a"))


def createSlug(title):
    slug_=""
    for i in title:
        if i!=" ":
            if ord(i)>=97:
                slug_+=i
            else:
                slug_+=chr(ord(i)+32)
        else:
            slug_+="-"
    return slug_

print(createSlug("The hii theri S"))