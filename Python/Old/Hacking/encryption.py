# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alpha = len(alphabet)

# def encrypt(plaintext, k):
#     newtext=''
#     for i in range(len(plaintext)):
#         # plaintext[i]=alphabet[i+k]
#         newtext=newtext+alphabet[i+k]
#         i=i+1
#     return print(newtext)
    
#    #pass # do stuff and return ciphertext
# samir='samir'
# encrypt(samir,1)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    alphaupdated=alphabet[26-k:]
    alphaupdated+=alphabet[0:26-k]
    #print(alphaupdated)
    newtext=''
    for i in plaintext:
        newindex=alphabet.index(i)
        newtext+=alphaupdated[newindex]
    return print(newtext)


   #pass # do stuff and return ciphertext

encrypt("samirpatil",10)

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
    sam=[]
    for i in range(0,26):
        k=(i)
        words=decrypt(ciphertext,k)
        print([i,words])
        list.append([i,words])
        # if (words=="vdplusdwlo"):
        #     sam.append(words)
        # else:
        #     sam.append("Nothing")
    return list
    # pass #print all (plaintext, k) possibilities and copy the right one to the Edx platform
sa="nT RGW DIEXW VW QURG TIY"
def fun(str):
    str_=""
    for i in str:
        if(65<=ord(i)<91):
            str_+=chr(ord(i)+32)
        else:
            str_+=i
    return str_

brute_force(fun(""))

# # sam="hm al, mo tmh hm al, huvh gn hul jzlnhgmt: qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo hul nxgtsn vty voomqn mr mzhovslmzn rmohztl, mo hm hvel vocn vsvgtnh v nlv mr homzaxln vty ak mppmngts lty hulc? hm ygl: hm nxllp; tm cmol; vty, ak v nxllp hm nvk ql lty hul ulvoh-vwul vty hul humznvty tvhzovx numwen huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt yldmzhxk hm al qgnu'y. hm ygl, hm nxllp; hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza; rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,cznh sgdl zn pvznl"
# def frequency(string):
#     string=string.split()
#     string2=[]
#     for i in string:
#         if i is not in string2:
#             string2.append(i)
#     return print(string2)
# frequency(sam)


# # Main file of the Python 3 program.

# from collections import OrderedDict 
# sam="hm al, mo tmh hm al, huvh gn hul jzlnhgmt: qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo hul nxgtsn vty voomqn mr mzhovslmzn rmohztl, mo hm hvel vocn vsvgtnh v nlv mr homzaxln vty ak mppmngts lty hulc? hm ygl: hm nxllp; tm cmol; vty, ak v nxllp hm nvk ql lty hul ulvoh-vwul vty hul humznvty tvhzovx numwen huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt yldmzhxk hm al qgnu'y. hm ygl, hm nxllp; hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza; rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,cznh sgdl zn pvznl"
# sam2=sam.replace(" ","")
# sam3=sam2.replace("'","")
# sam4=sam3.replace(":","")
# sam5=sam4.replace(";","")
# sam6=sam5.replace(",","")
# sam7=sam6.replace("?","")
# sam8=sam7.replace("-","")
# sam9=sam8.replace(".","")
# #print(sam9)
# def frequency(string):
#     dict={}
    
#     for i in string:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=1
            
     
#     return str(dict)
# print(frequency(sam9))

#     # dict= OrderedDict()
#     # for key,values in dict.items():
#     #     print(key,value)



