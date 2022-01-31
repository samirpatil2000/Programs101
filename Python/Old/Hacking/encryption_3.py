# import string, random
#
# # ============ Word List Gen ============
# minimum = int(input('Please enter the minimum length of any give word to be generated: '))
# maximum = int(input('Please enter the maximum length of any give word to be generated: '))
# wmaximum = int(input('Please enter the max number of words to be generate in the dictionary: '))
#
# alphabet = string.capwords[0:52] + string.digits + string.punctuation
# string = ''
# FILE = open("wl.txt", "w")
# for count in range(0, wmaximum):
#     for x in random.sample(alphabet, random.randint(minimum, maximum)):
#         string += x
#     FILE.write(string + '\n')
#     string = ''
# FILE.close()
# print  ('DONE!')

def lowercase():
    lowercaseList=[]
    for i in range(97,123):
        lowercaseList.append(chr(i))
    print(lowercaseList)

def uppercase():
    uppercaseList=[]
    for i in range(65,91):
        uppercaseList.append(chr(i))
    print(uppercaseList)


alphalist=lowercase()
encrypted_alphabet = '@bcd;fgh*j&lmno$qrst!vw+=z'







