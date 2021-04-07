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