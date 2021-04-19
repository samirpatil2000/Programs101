
print(ord('Z'),ord('a'))
def pangram(s):
    word_dict={chr(i):0 for i in range(65,91)}
    # print(word_dict)
    for i in s:
        if(i.isalpha()):
            word_dict[i.upper()]=1
    print(word_dict)
    for i in word_dict.values():
        if(i==0):
            return False
    return True
    
    
print(pangram("We promptly judged antique ivory buckles for the next prize"))
# print("s".isalpha())