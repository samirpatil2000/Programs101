
def cipher(s,k):
    while(k>26):
        k-=26
    original_alpha="abcdefghijklmnopqrstuvwxyz"
    encrypted_alpha=original_alpha[k:]+original_alpha[0:k]
    new_str=''
    for str_ in s:
        if str_.isalpha():
            if(str_.islower()):
                new_str+=encrypted_alpha[ord(str_)-ord('a')]
            else:
                new_str+=encrypted_alpha[ord(str_.lower())-ord('a')].upper()
        else:
            new_str+=str_
    # print(encrypted_alpha)
    return new_str
    

# sam_="samirpatil"
# print(sam_[2:]+sam_[0:2])

print(cipher("There's-a-starman-waiting-in-the-sky",3))

