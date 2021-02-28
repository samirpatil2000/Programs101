
count=0
def printPermutation(str,output_str):
    if(len(str)==0):
        print("Sam....")
        print("    ...")
        print(output_str)
        return
    
    for i in range(len(str)):
        ch=str[i]
        rem=str[0:i]+str[i+1:]
        printPermutation(rem,output_str+ch)
    
printPermutation("ABC","")

# print(count)
# str="ABCD"
# print(str[0:2]+str[2+1:])