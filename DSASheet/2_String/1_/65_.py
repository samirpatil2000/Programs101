def printSubsequnce(input_str,output_str):
    if(len(input_str)==0):
        print(output_str)
        return
    printSubsequnce(input_str[1:],output_str+"")
    printSubsequnce(input_str[1:],output_str+input_str[0])

printSubsequnce("abc","")