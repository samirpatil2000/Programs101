def sortString(s):
    frequency_arr=[0 for _ in range(26)]
    for i in s:
        frequency_arr[ord(i)-97]+=1
    k=0
    str_=""
    while(k<len(s)):
        j=0
        while(j<26):
            if(frequency_arr[j] !=0):
                frequency_arr[j]-=1
                str_+=chr(j+97)
                k+=1
            j+=1
        j-=1
        while(j>=0):
            if(frequency_arr[j] !=0):
                frequency_arr[j]-=1
                str_+=chr(j+97)
                k+=1
            j-=1
    return str_    
        
    

s="aaaabbbbcccc"
print(sortString(s))