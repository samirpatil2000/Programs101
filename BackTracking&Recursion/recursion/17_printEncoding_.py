
arr=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def printEncoding(input_str,output_str):
    
    if(len(input_str)==0):
        print(output_str)
        return
    if(len(input_str)==1):
        if(int(input_str)==0):
            return
        else:
            print(output_str+arr[int(input_str)])
            return
    else:
        if(int(input_str[:2])<=26):
            printEncoding(input_str[2:],output_str+arr[int(input_str[:2])])
        printEncoding(input_str[1:],output_str+arr[int(input_str[0])])
            
        
# str="Samir"
# print(str[1:])

printEncoding("12","")