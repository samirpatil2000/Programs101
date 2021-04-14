print(ord('A'),ord('S')+32,[ord('s')-ord('S')])
print(chr(14))

print(ord('Z'))
def fun(str):
    str_=""
    for i in str:
        if(65<=ord(i)<91):
            str_+=chr(ord(i)+32)
        else:
            str_+=i
    return str_

print(fun("VXOBGZK"))
            