alphabet=' abcdefghijklmnopqrstuvwxyz'
encrypted_alphabet=' #=~*-f^`&j?}m.+,q>@t{v%x\|'


def encryption(text,key):
    encrypted_alphupdated = encrypted_alphabet[26-key:]
    encrypted_alphupdated += encrypted_alphabet[0:26-key]
    encrypted_text=''

    for i in text:
        newindex=alphabet.index(i)
        encrypted_text+=encrypted_alphupdated[newindex]
    return encrypted_text
text=input("Enter the message here : ")
for_decryption=encryption(text,0)
print(for_decryption)


def decryption(text,key):
    decrypted_alphaupdated= encrypted_alphabet[26-key:]
    decrypted_alphaupdated+=encrypted_alphabet[0:26-key]

    original_text=''
    for i in text:
        newindex=decrypted_alphaupdated.index(i)
        original_text+=alphabet[newindex]
    return print(original_text)


decryption(for_decryption,0)




