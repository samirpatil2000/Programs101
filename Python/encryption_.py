alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    alphaupdated=alphabet[26-k:]
    alphaupdated+=alphabet[0:26-k]
    newtext=''
    for i in plaintext:
        newindex=alphabet.index(i)
        newtext+=alphaupdated[newindex]
    return newtext


# encrypt("samirpatil",10)

def decrypt(plaintext,k):
    alphaupdated=alphabet[26-k:]
    alphaupdated+=alphabet[0:26-k]
    originaltext=''
    for i in plaintext:
        originalindex=alphaupdated.index(i)
        originaltext+=alphabet[originalindex]
    return originaltext


decrypt("iqcyhfqjyb",10)
print('this is a brute_force  \n')

def brute_force(ciphertext):
    list=[]
    for i in range(0,26):
        k=(i)
        words=decrypt(ciphertext,k)
        # print([i,words])
        list.append([i,words])
    return list

sa="nT RGW DIEXW VW QURG TIY"
def lowerCase(str):
    str_=""
    for i in str:
        if(65<=ord(i)<91):
            str_+=chr(ord(i)+32)
        else:
            str_+=i
    return str_


# print(brute_force("DIEXW"))

dict_=[[]]

i=0
while(i<len(sa)):
    str_=""
    while(i<len(sa) and sa[i]!=" "):
        str_+=sa[i]
        i+=1
    i+=1
    list=brute_force(lowerCase(str_))
    dict_.append(list)

print(dict_)

# for line in range(len(dict_)):
    
    




# def password_reset(request: HttpRequest) -> HttpResponse:
#     view_func = DjangoPasswordResetView.as_view(
#         template_name="zerver/reset.html",
#         form_class=ZulipPasswordResetForm,
#         success_url="/accounts/password/reset/done/",
        # initial={
        #     "email":request.user.email
        # }
#     )
#     return view_func(request)