def printSubSeq(input_str,output_str):
    if(len(input_str)==0):
        print(output_str)
        return 
    ch=input_str[0]
    rem=input_str[1:]
    printSubSeq(rem,output_str+ch)
    printSubSeq(rem,output_str+"")
    
    
printSubSeq("MAD","")