



def textToNum(input_arr,arr):
    output=''
    for i in input_arr:
        if i==' ':
            output+=0
        else:
            ch=ord(i)-ord('A')
            output+=arr[ch]
    return output


str_=['2','22','222','3','33','333',
    '4','44','444','5','55','555',
    '6','66','666','7','77','777','7777'
    '8','88','888','9','99','999','9999']


text="GEEKSFORGEEKS"
print(textToNum(text,str_))